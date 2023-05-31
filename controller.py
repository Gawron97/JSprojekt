import datetime

from dateutil.relativedelta import relativedelta

import exceptions.exceptions as ex
from model import Model
from tables.category import Category
from tables.type import Type
from view.add_transaction_view import AddTransactionView
from view.stats_view import StatsView
from view.view import View


class Controller:

    def __init__(self, view: View, outcome_model: Model):
        self.view: View = view
        self.model: Model = outcome_model

        self.date = datetime.datetime.now()
        self.current_spent_amount = outcome_model.get_spent_amount_in_month(self.date)

        self.on_buttons_click()
        self.load_outcomes()
        self.update_progress_bar()
        self.update_chart()
        self.update_limit_label()
        self.view.set_actual_year(self.date)


    def on_buttons_click(self):
        self.view.ui.outcomesButton.clicked.connect(self.load_outcomes)
        self.view.ui.incomesButton.clicked.connect(self.load_incomes)
        self.view.ui.setLimitButton.clicked.connect(self.set_limit)
        self.view.ui.addTransactionButton.clicked.connect(self.add_transaction)
        self.view.ui.prevMonthButton.clicked.connect(self.previous_month)
        self.view.ui.nextMonthButton.clicked.connect(self.next_month)
        self.view.ui.detailStatsButton.clicked.connect(self.details_statistics)

    def update_progress_bar(self):
        self.view.edit_progress_bar(self.model.get_spent_amount_in_month(self.date), self.model.get_limit_in_month(self.date))

    def update_chart(self):
        expenses_by_category = self.model.get_spent_amount_by_categories(self.date)
        self.view.edit_chart(expenses_by_category)

    def show_data_in_list(self, data):
        self.view.set_data(data)

    def load_outcomes(self):
        data = self.model.get_outcomes_in_month(self.date)
        self.show_data_in_list(data)
        amount_spent_in_month = self.model.get_spent_amount_in_month(self.date)
        self.view.update_amount_of_money_label("amount spent: ", amount_spent_in_month)

    def load_incomes(self):
        data = self.model.get_incomes_in_month(self.date)
        self.show_data_in_list(data)
        earned_amount_in_month = self.model.get_earned_amount_in_month(self.date)
        self.view.update_amount_of_money_label("amount earned: ", earned_amount_in_month)

    def update_chart_layout(self):
        self.update_progress_bar()
        self.update_chart()
        self.update_limit_label()

    def update_limit_label(self):
        limit_amount = self.model.get_limit_in_month(self.date)
        self.view.update_limit_label(limit_amount)

    def set_limit(self):
        limit = self.view.ui.limitLineEdit.text()
        try:
            self.model.update_limit_for_month(limit, self.date)
        except ex.WrongLimitException as e:
            self.view.show_limit_error_msg(e.message)

        self.update_chart_layout()
        self.update_limit_label()
        self.view.ui.limitLineEdit.setText('')

    def add_transaction(self):
        self.add_transaction_view = AddTransactionView()
        self.add_transaction_view.init_category_combo_box([Category.FOOD.name, Category.TRANSPORTATION.name,
                                                           Category.HOUSEHOLD.name, Category.ENTERTAINMENT.name,
                                                           Category.INVESTMENT.name, Category.OTHER.name])
        self.add_transaction_view.init_type_combo_box([Type.OUTCOME.name, Type.INCOME.name])
        self.add_transaction_view.ui.submitButton.clicked.connect(self.submit_transaction)
        self.add_transaction_view.exec_()

    def submit_transaction(self):
        try:
            self.model.add_transaction(self.add_transaction_view.ui.nameLineEdit.text(),
                                       self.add_transaction_view.ui.priceLineEdit.text(),
                                       self.add_transaction_view.ui.dateLineEdit.text(),
                                       self.add_transaction_view.ui.categoryComboBox.currentText(),
                                       self.add_transaction_view.ui.typeComboBox.currentText(),
                                       self.date)

            if self.add_transaction_view.ui.typeComboBox.currentText() == Type.OUTCOME.name:
                self.load_outcomes()
                self.update_chart_layout()
            else:
                self.load_incomes()

            self.add_transaction_view.close()

        except Exception as e:
            self.add_transaction_view.show_incorrect_data_msg(e.message)

    def previous_month(self):
        self.date = self.date - relativedelta(months=1)
        self.load_outcomes()
        self.update_chart_layout()
        self.view.set_actual_year(self.date)

    def next_month(self):
        self.date = self.date + relativedelta(months=1)
        self.load_outcomes()
        self.update_chart_layout()
        self.view.set_actual_year(self.date)

    def details_statistics(self):
        self.details_statistics_view = StatsView()
        expanses_in_each_month = self.model.get_expanses_in_each_month(self.date)
        incomes_in_each_month = self.model.get_incomes_in_each_month(self.date)
        difference_between_expanses_and_limit = self.model.get_difference_in_limit_and_expanses(self.date)
        self.details_statistics_view.update_data(expanses_in_each_month, incomes_in_each_month,
                                                 difference_between_expanses_and_limit)
        self.details_statistics_view.exec_()


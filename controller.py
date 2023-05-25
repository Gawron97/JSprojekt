import datetime

from dateutil.relativedelta import relativedelta

import exceptions.exceptions as ex
from model import Model
from view.add_transaction_view import AddTransactionView
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


    def on_buttons_click(self):
        self.view.ui.outcomesButton.clicked.connect(self.load_outcomes)
        self.view.ui.incomesButton.clicked.connect(self.load_incomes)
        self.view.ui.setLimitButton.clicked.connect(self.set_limit)
        self.view.ui.addTransactionButton.clicked.connect(self.add_transaction)
        self.view.ui.prevMonthButton.clicked.connect(self.previous_month)
        self.view.ui.nextMonthButton.clicked.connect(self.next_month)


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

    def load_incomes(self):
        data = self.model.get_incomes_in_month(self.date)
        self.show_data_in_list(data)

    def update_chart_layout(self):
        self.update_progress_bar()
        self.update_chart()

    def set_limit(self):
        limit = self.view.ui.limitLineEdit.text()
        try:
            self.model.update_limit_for_month(limit, self.date)
        except ex.WrongLimitException as e:
            self.view.show_limit_error_msg(e.message)

        self.update_chart_layout()
        self.view.ui.limitLineEdit.setText('')

    def add_transaction(self):
        self.add_transaction_view = AddTransactionView()
        self.add_transaction_view.ui.submitButton.clicked.connect(self.submit_transaction)
        self.add_transaction_view.exec_()

    def submit_transaction(self):
        try:
            self.model.add_transaction(self.add_transaction_view.ui.nameLineEdit.text(),
                self.add_transaction_view.ui.priceLineEdit.text(), self.add_transaction_view.ui.dateLineEdit.text(),
                self.add_transaction_view.ui.categoryLineEdit.text(), self.add_transaction_view.ui.typeLineEdit.text())

            self.load_outcomes()
            self.update_chart_layout()
            self.add_transaction_view.close()
        except ex.IncorrectTypeError as e:
            self.add_transaction_view.show_incorrect_data_msg(e.message)
        except ex.IncorrectCategoryException as e:
            self.add_transaction_view.show_incorrect_data_msg(e.message)
        except ex.WrongPriceException as e:
            self.add_transaction_view.show_incorrect_data_msg(e.message)
        except ex.WrongDateError as e:
            self.add_transaction_view.show_incorrect_data_msg(e.message)

    def previous_month(self):
        self.date = self.date - relativedelta(months=1)
        self.load_outcomes()
        self.update_chart_layout()

    def next_month(self):
        self.date = self.date + relativedelta(months=1)
        self.load_outcomes()
        self.update_chart_layout()


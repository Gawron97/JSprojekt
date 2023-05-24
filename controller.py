import datetime

from model import Model
from view import View


class Controller:

    def __init__(self, view: View, outcome_model: Model):
        self.view: View = view
        self.model: Model = outcome_model

        self.date = datetime.datetime.now()
        self.current_spent_amount = outcome_model.get_spent_amount_in_month(self.date)

        self.on_buttons_click()
        self.update_data()
        self.update_progress_bar()
        self.update_chart()


    def on_buttons_click(self):
        self.view.ui.outcomesButton.clicked.connect(self.load_outcomes)
        self.view.ui.incomesButton.clicked.connect(self.load_incomes)
        self.view.ui.setLimitButton.clicked.connect(self.set_limit)

    def update_data(self):
        self.load_outcomes()

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

    def set_limit(self):
        limit = self.view.ui.limitLineEdit.text()
        try:
            self.model.update_limit_for_month(limit, self.date)
        except Exception:
            self.view.show_limit_error_msg()

        self.update_progress_bar()
        self.update_chart()


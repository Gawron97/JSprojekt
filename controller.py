import sys

from income_service import IncomeService
from view import View


class Controller:

    def __init__(self, view: View, income_model: IncomeService):
        self.view: View = view
        self.income_model: IncomeService = income_model

    def start(self):
        self.view.start()



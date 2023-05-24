from category import Category
from repository import Repository


class Model:

    def __init__(self, repository: Repository):
        self.repository: Repository = repository


    def add_transaction(self):
        self.repository.add_transaction()

    def add_limit(self):
        self.repository.add_limit()

    def get_limit_in_month(self, date):
        limit = self.repository.get_limit_in_month(date)
        return limit.amount if limit else 0

    def get_outcomes_in_month(self, date):
        return self.repository.get_outcomes_in_month(date)

    def get_incomes_in_month(self, date):
        return self.repository.get_incomes_in_month(date)

    def get_spent_amount_in_month(self, date):
        return self.repository.get_spent_amount_in_month(date)

    def update_limit_for_month(self, limit, date):

        try:
            limit_int = int(limit)
        except Exception:
            raise Exception


        if limit_int <= 0 or limit_int <= self.get_spent_amount_in_month(date):
            raise Exception

        if self.repository.get_limit_in_month(date):
            self.repository.update_limit(limit_int, date)
        else:
            self.repository.add_limit(limit_int, date)

    def get_spent_amount_by_categories(self, date):
        expenses_by_category = {
            'FOOD': self.repository.get_spent_amount_in_month_by_category(date, Category.FOOD),
            'ENTERTAINMENT': self.repository.get_spent_amount_in_month_by_category(date, Category.ENTERTAINMENT),
            'INVESTMENT': self.repository.get_spent_amount_in_month_by_category(date, Category.INVESTMENT),
            'HOUSEHOLD': self.repository.get_spent_amount_in_month_by_category(date, Category.HOUSEHOLD),
            'TRANSPORTATION': self.repository.get_spent_amount_in_month_by_category(date, Category.TRANSPORTATION),
            'OTHER': self.repository.get_spent_amount_in_month_by_category(date, Category.OTHER)
        }
        limit_DB = self.repository.get_limit_in_month(date)
        limit = limit_DB.amount if limit_DB else 0 - self.repository.get_spent_amount_in_month(date)
        if limit > 0:
            expenses_by_category['LIMIT'] = limit

        return expenses_by_category

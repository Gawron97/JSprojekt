import datetime
from typing import List

from tables.category import Category
from tables.entities import Transaction
from database.repository import Repository
from tables.type import Type
import exceptions.exceptions as ex


class Model:

    def __init__(self, repository: Repository):
        self.repository: Repository = repository


    # def add_transaction(self):
    #     self.repository.add_transaction()

    def add_limit(self):
        self.repository.add_limit()

    def get_limit_in_month(self, date):
        limit = self.repository.get_limit_in_month(date)
        return limit.amount if limit else 0

    def get_outcomes_in_month(self, date):
        data: List[Transaction] = self.repository.get_outcomes_in_month(date)
        data.sort(key=lambda data: data.date)
        return data

    def get_incomes_in_month(self, date):
        return self.repository.get_incomes_in_month(date)

    def get_spent_amount_in_month(self, date):
        return self.repository.get_spent_amount_in_month(date)

    def update_limit_for_month(self, limit, date):

        try:
            limit_int = int(limit)
        except Exception:
            raise ex.WrongLimitException("Provided limit is not correct")

        if limit_int <= 0 or limit_int <= self.get_spent_amount_in_month(date):
            raise ex.WrongLimitException('Provided limit should be higher then already spend amount in this month and'
                                         ' higher than 0')

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
        limit = (limit_DB.amount if limit_DB else 0) - self.repository.get_spent_amount_in_month(date)
        if limit > 0:
            expenses_by_category['LIMIT'] = limit

        return expenses_by_category

    def add_transaction(self, name, price, date, category, type):

        try:
            price_int = int(price)
            if price_int <= 0:
                raise Exception
        except Exception:
            raise ex.WrongPriceException('provided price is not correct')

        try:
            formated_date = datetime.datetime.strptime(date, "%d-%m-%Y")
        except Exception:
            raise ex.WrongDateError('Provided date is not correct, format should be d-M-Y')

        if formated_date > datetime.datetime.now():
            raise ex.WrongDateError('Provided date is not correct, date cannot be after today')

        try:
            formated_category = Category(category)
        except:
            raise ex.IncorrectCategoryException('Provided category is not correct')
        try:
            formated_type = Type(type)
        except:
            raise ex.IncorrectTypeError('Provided type is not correct')

        transaction = Transaction(name, price_int, formated_date, formated_category, formated_type)
        self.repository.add_transaction(transaction)

    def get_expanses_in_each_month(self, date):
        return self.prepare_data(self.repository.get_sum_price_outcomes_for_each_month(date))

    def get_incomes_in_each_month(self, date):
        return self.prepare_data(self.repository.get_sum_of_incomes_for_each_month(date))

    def get_difference_in_limit_and_expanses(self, date):
        limit_in_each_month = self.prepare_data(self.repository.get_limit_in_each_month(date))
        expanses_in_each_month = self.prepare_data(self.repository.get_sum_price_outcomes_for_each_month(date))

        print(limit_in_each_month)
        print(expanses_in_each_month)

        result = []
        for i in range(0, 12, 1):
            result.append((i+1, max(limit_in_each_month[i][1] - expanses_in_each_month[i][1], 0)))

        return result


    def prepare_data(self, data):
        result = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0)]
        for row in data:
            result[int(row[0]) - 1] = (int(row[0]), row[1])

        return result


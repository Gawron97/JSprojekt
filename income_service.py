import datetime

from category import Category
from entities import Income
from database import session


class IncomeService:

    def add_income(self):
        income = Income(name='testowy', price=10.0, date=datetime.datetime.now(), category=Category.FOOD)
        session.add(income)
        session.commit()

    def get_all_incomes(self):
        return session.query(Income).all()
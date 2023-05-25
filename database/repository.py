from sqlalchemy import extract, func, and_

from database.database import session
from tables.entities import Transaction, Limit
from tables.type import Type


class Repository:

    def add_transaction(self, transaction):
        session.add(transaction)
        session.commit()

    def add_limit(self):
        limit = Limit(year=2023, month=5, amount=200)
        session.add(limit)
        session.commit()

    def get_limit_in_month(self, date):
        return session.query(Limit).filter(
            and_(
                Limit.year == date.year,
                Limit.month == date.month
            )
        ).first()

    def get_outcomes_in_month(self, date):
        return session.query(Transaction).filter(
            and_(
                Transaction.type == Type.OUTCOME,
                extract('month', Transaction.date) == date.month,
                extract('year', Transaction.date) == date.year
            )
        ).all()

    def get_incomes_in_month(self, date):
        return session.query(Transaction).filter(
            and_(
                Transaction.type == Type.INCOME,
                extract('month', Transaction.date) == date.month,
                extract('year', Transaction.date) == date.year
            )
        ).all()

    def get_spent_amount_in_month(self, date):
        res = session.query(func.sum(Transaction.price)).filter(
            and_(
                Transaction.type == Type.OUTCOME,
                extract('month', Transaction.date) == date.month,
                extract('year', Transaction.date) == date.year
            )
        ).scalar()
        return res if res else 0

    def update_limit(self, new_amount, date):
        session.query(Limit).filter(Limit.year == date.year, Limit.month == date.month).update({"amount": new_amount})
        session.commit()

    def add_limit(self, new_amount, date):
        limit = Limit(year=date.year, month=date.month, amount=new_amount)
        session.add(limit)
        session.commit()

    def get_spent_amount_in_month_by_category(self, date, category):
        res = session.query(func.sum(Transaction.price)).filter(
            and_(
                Transaction.type == Type.OUTCOME,
                Transaction.category == category,
                extract('month', Transaction.date) == date.month,
                extract('year', Transaction.date) == date.year
            )
        ).scalar()

        return res if res else 0

from sqlalchemy import extract, func, and_

from database.database import session
from tables.entities import Transaction, Limit
from tables.type import Type


class Repository:

    def add_transaction(self, transaction):
        session.add(transaction)
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
        return self.get_amount_in_month(date, Type.OUTCOME)

    def get_earned_amount_in_month(self, date):
        return self.get_amount_in_month(date, Type.INCOME)

    def get_amount_in_month(self, date, transaction_type):
        res = session.query(func.sum(Transaction.price)).filter(
            and_(
                Transaction.type == transaction_type,
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

    def get_sum_price_outcomes_for_each_month(self, date):
        return session.query(
            extract('month', Transaction.date).label('month'),
            func.coalesce(func.sum(Transaction.price), 0).label('total_expenses')
        ).filter(
            extract('year', Transaction.date) == date.year,
            Transaction.type == Type.OUTCOME
        ).group_by(
            extract('month', Transaction.date)
        ).all()

    def get_sum_of_incomes_for_each_month(self, date):
        return session.query(
            extract('month', Transaction.date).label('month'),
            func.coalesce(func.sum(Transaction.price), 0).label('total_expenses')
        ).filter(
            extract('year', Transaction.date) == date.year,
            Transaction.type == Type.INCOME
        ).group_by(
            extract('month', Transaction.date)
        ).all()

    def get_limit_in_each_month(self, date):
        return session.query(
            Limit.month.label('month'),
            Limit.amount.label('amount')
        ).filter(
            Limit.year == date.year
        ).all()

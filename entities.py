from sqlalchemy import Column, Integer, String, DateTime, Double, Enum
from category import Category
from database import Base
from type import Type


class Transaction(Base):
    __tablename__ = 'transactions'
    id_income = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Double(precision=2))
    date = Column(DateTime)
    category = Column(Enum(Category))
    type = Column(Enum(Type))

    def to_string(self):
        return f'{self.id_income} {self.name} {self.price} {self.date} {self.category}'


class Limit(Base):
    __tablename__ = 'limits'
    year = Column(Integer, primary_key=True)
    month = Column(Integer, primary_key=True)
    amount = Column(Double(precision=2))

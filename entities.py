from sqlalchemy import Column, Integer, String, DateTime, Double, Enum
from category import Category
from database import Base


class Income(Base):
    __tablename__ = 'incomes'
    id_income = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Double(precision=2))
    date = Column(DateTime)
    category = Column(Enum(Category))

    def to_string(self):
        return f'{self.id_income} {self.name} {self.price} {self.date} {self.category}'


class Outcome(Base):
    __tablename__ =  'outcomes'
    id_outcome = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Double(precision=2))
    date = Column(DateTime)


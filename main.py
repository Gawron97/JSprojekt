import random

from database import database_config
from database.repository import Repository
from controller import Controller
from model import Model
from view.view import View
import sys
from PyQt5.QtWidgets import QApplication


database_config.database_config()

repository = Repository()
model = Model(repository)

app = QApplication(sys.argv)
view = View()

controller = Controller(view, model)


view.show()
sys.exit(app.exec_())

# transactions = [{
#     'name': 'Książka',
#     'category': "ENTERTAINMENT"
# }, {
#     'name': 'Pizza',
#     'category': "FOOD"
# }, {
#     'name': 'Pralka',
#     'category': "HOUSEHOLD"
# }, {
#     'name': 'Suszrka',
#     'category': "HOUSEHOLD"
# }, {
#     'name': 'Grzyby',
#     'category': "FOOD"
# }, {
#     'name': 'Mięso',
#     'category': "FOOD"
# }, {
#     'name': 'Ser',
#     'category': "FOOD"
# }, {
#     'name': 'Pilot',
#     'category': "HOUSEHOLD"
# }, {
#     'name': 'Banknot',
#     'category': "INVESTMENT"
# }, {
#     'name': 'Akcje',
#     'category': "INVESTMENT"
# }, {
#     'name': 'Film',
#     'category': "ENTERTAINMENT"
# }, {
#     'name': 'Kino',
#     'category': "ENTERTAINMENT"
# }, {
#     'name': 'Gra',
#     'category': "ENTERTAINMENT"
# }, {
#     'name': 'Autobus',
#     'category': "TRANSPORTATION"
# }, {
#     'name': 'Aparat',
#     'category': "ENTERTAINMENT"
# }, {
#     'name': 'Młotek',
#     'category': "HOUSEHOLD"
# },{
#     'name': 'Drewno',
#     'category': "HOUSEHOLD"
# }, {
#     'name': 'Kubek',
#     'category': "INVESTMENT"
# }]
#
# for i in range(1, 200):
#     selected = random.choice(transactions)
#     print(selected['name'])
#     print(random.randint(10, 200))
#     day = random.randint(1, 28)
#     day_s = f'{day}'
#     if day < 10:
#         day_s = f'{0}{day}'
#     month = random.randint(1, 12)
#     mon_s = f'{month}'
#     if month < 10:
#         mon_s = f'{0}{month}'
#     date = f'{day_s}-{mon_s}-{random.randint(2022, 2022)}'
#     print(date)
#     print(selected['category'])
#     model.add_transaction(selected['name'], random.randint(10, 200), date, selected['category'], 'OUTCOME')

# for i in range(1, 100):
#     model.add_transaction(random.choice(transactions)['name'])
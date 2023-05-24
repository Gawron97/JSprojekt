
import database_config
from repository import Repository
from controller import Controller
from model import Model
from view import View
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

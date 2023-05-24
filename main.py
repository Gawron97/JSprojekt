import database_config
from income_service import IncomeService
from controller import Controller
from view import View


database_config.database_config()

income_service = IncomeService()
view = View()

controller = Controller(view, income_service)
controller.start()

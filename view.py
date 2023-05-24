from PyQt5.QtChart import QPieSeries
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from ui.main_view import Ui_MainView


class View(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainView()
        self.ui.setupUi(self)


    def set_data(self, data):
        self.ui.budgetList.clear()
        self.ui.budgetList.addItems(row.to_string() for row in data)

    def set_limit(self, new_limit):
        self.ui.progress_bar.setRange(0, new_limit)

    def edit_progress_bar(self, current_value, max_value):
        self.ui.progress_bar.setRange(0, max_value)
        self.ui.progress_bar.setValue(current_value)

    def edit_chart(self, expenses_by_category: dict):
        series = QPieSeries()
        for category, expense in expenses_by_category.items():
            series.append(category, expense)

        self.ui.chart.removeAllSeries()
        self.ui.chart.addSeries(series)


    def show_limit_error_msg(self):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Information)
        error_msg.setWindowTitle('Bad limit')
        error_msg.setText('Provided limit is incorrect')
        error_msg.setStandardButtons(QMessageBox.Ok)
        error_msg.exec()

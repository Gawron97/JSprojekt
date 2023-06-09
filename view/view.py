from PyQt5.QtChart import QPieSeries, QPieSlice
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem

from ui.main_view import Ui_MainView


class View(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainView()
        self.ui.setupUi(self)


    def set_data(self, data):
        self.ui.budgetList.clear()
        for row in data:
            item = QListWidgetItem()
            item.setData(Qt.UserRole, row)
            self.ui.budgetList.addItem(item)

    def edit_progress_bar(self, current_value, max_value):
        self.ui.progress_bar.reset()
        self.ui.progress_bar.setRange(0, max_value)
        self.ui.progress_bar.setValue(current_value)

    def edit_chart(self, expenses_by_category: dict):
        series = QPieSeries()
        i=0
        for category, expense in expenses_by_category.items():
            series.append(category, expense)
            series.slices()[i].setLabelColor(QColor("#800000"))
            i += 1

        series.setLabelsVisible(True)
        series.setLabelsPosition(QPieSlice.LabelInsideNormal)
        self.ui.chart.removeAllSeries()
        self.ui.chart.addSeries(series)

    def set_actual_year(self, date):
        self.ui.dateLabel.setText(f'actual date: {date.month}-{date.year}')

    def show_limit_error_msg(self, message):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Information)
        error_msg.setWindowTitle('Bad limit')
        error_msg.setText(message)
        error_msg.setStandardButtons(QMessageBox.Ok)
        error_msg.exec()

    def update_amount_of_money_label(self, text, spent_amount):
        self.ui.amount_of_money.setText(f'{text}{spent_amount}')

    def update_limit_label(self, limit_amount):
        self.ui.monthLimitLabel.setText(f'Limit in this month: {limit_amount}')

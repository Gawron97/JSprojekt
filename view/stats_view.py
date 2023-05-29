from PyQt5.QtChart import QChart, QBarSeries, QBarCategoryAxis, QLineSeries, QChartView, QBarSet, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ui.stats_view import Ui_StatsPanel


class StatsView(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_StatsPanel()
        self.ui.setupUi(self)

    def update_data(self, expanses_in_each_month, incomes_in_each_month, difference_between_expanses_and_limit):
        self.update_chart(expanses_in_each_month, incomes_in_each_month, difference_between_expanses_and_limit)
        yearly_income = sum(income[1] for income in incomes_in_each_month)
        yearly_outcome = sum(outcome[1] for outcome in expanses_in_each_month)
        self.update_labels(yearly_income, yearly_outcome)

    def update_chart(self, expanses_in_each_month, incomes_in_each_month, difference_between_expanses_and_limit):
        serie = QBarSet('outcomes')
        for row in expanses_in_each_month:
            serie.append(row[1])

        serie2 = QBarSet('incomes')
        for row in incomes_in_each_month:
            serie2.append(row[1])

        series = QBarSeries()
        series.append(serie)
        series.append(serie2)

        categories = ['Jan', 'Feb', 'March', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        axis = QBarCategoryAxis()
        axis.append(categories)

        self.ui.chart.addSeries(series)
        self.ui.chart.setAxisX(axis, series)

        axis_y = QValueAxis()
        axis_y_max_value = self.calculate_axis_y_max_value(expanses_in_each_month, incomes_in_each_month)
        axis_y.setRange(0, axis_y_max_value)
        axis_y.applyNiceNumbers()

        self.ui.chart.addAxis(axis_y, Qt.AlignLeft)

        line_series = QLineSeries()
        for row in difference_between_expanses_and_limit:
            line_series.append(row[0], row[1])

        self.ui.chart.addSeries(line_series)

    def update_labels(self, yearly_income, yearly_outcome):
        self.ui.yearlyIncomeLabel.setText(f"Income in this year: {yearly_income}")
        self.ui.yearlyOutcomeLabel.setText(f"Outcome in this year: {yearly_outcome}")

    def calculate_axis_y_max_value(self, expanses_in_each_month, incomes_in_each_month):
        max_income = max(income[1] for income in incomes_in_each_month)
        max_outcome = sum(outcome[1] for outcome in expanses_in_each_month)

        return int(max(max_outcome, max_income))



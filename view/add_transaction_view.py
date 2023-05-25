from PyQt5.QtWidgets import QDialog, QMessageBox

from ui.add_transaction_view import Ui_AddTransaction


class AddTransactionView(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AddTransaction()
        self.ui.setupUi(self)

    def show_incorrect_data_msg(self, message):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Information)
        error_msg.setWindowTitle('Error while adding transaction')
        error_msg.setText(message)
        error_msg.setStandardButtons(QMessageBox.Ok)
        error_msg.exec()

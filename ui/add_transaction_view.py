# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_transaction.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTransaction(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(755, 593)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 19, 701, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.titleLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.titleLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.titleLabel.setMaximumHeight(15)
        self.titleLabel.setObjectName("titleLabel")
        self.mainLayout.addWidget(self.titleLabel)
        self.firstRow = QtWidgets.QHBoxLayout()
        self.firstRow.setObjectName("firstRow")
        self.nameLayout = QtWidgets.QVBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.nameLabel.setMaximumHeight(15)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLayout.addWidget(self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLayout.addWidget(self.nameLineEdit)
        self.firstRow.addLayout(self.nameLayout)
        self.priceLayout = QtWidgets.QVBoxLayout()
        self.priceLayout.setObjectName("priceLayout")
        self.priceLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.priceLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.priceLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.priceLabel.setMaximumHeight(15)
        self.priceLabel.setObjectName("priceLabel")
        self.priceLayout.addWidget(self.priceLabel)
        self.priceLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.priceLineEdit.setObjectName("priceLineEdit")
        self.priceLayout.addWidget(self.priceLineEdit)
        self.firstRow.addLayout(self.priceLayout)
        self.mainLayout.addLayout(self.firstRow)
        self.secondRow = QtWidgets.QHBoxLayout()
        self.secondRow.setObjectName("secondRow")
        self.dateLayout = QtWidgets.QVBoxLayout()
        self.dateLayout.setObjectName("dateLayout")
        self.dateLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dateLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.dateLabel.setMaximumHeight(15)
        self.dateLabel.setObjectName("dateLabel")
        self.dateLayout.addWidget(self.dateLabel)
        self.dateLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.dateLineEdit.setPlaceholderText("np. 15-04-2023")
        self.dateLineEdit.setObjectName("dateLineEdit")
        self.dateLayout.addWidget(self.dateLineEdit)
        self.secondRow.addLayout(self.dateLayout)
        self.categoryLayout = QtWidgets.QVBoxLayout()
        self.categoryLayout.setObjectName("categoryLayout")
        self.categoryLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.categoryLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.categoryLabel.setMaximumHeight(15)
        self.categoryLabel.setObjectName("categoryLabel")
        self.categoryLayout.addWidget(self.categoryLabel)
        self.categoryLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.categoryLineEdit.setObjectName("categoryLineEdit")
        self.categoryLayout.addWidget(self.categoryLineEdit)
        self.secondRow.addLayout(self.categoryLayout)
        self.mainLayout.addLayout(self.secondRow)
        self.thirdRow = QtWidgets.QHBoxLayout()
        self.thirdRow.setObjectName("thirdRow")
        self.typeLayout = QtWidgets.QVBoxLayout()
        self.typeLayout.setObjectName("typeLayout")
        self.typeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.typeLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.typeLabel.setMaximumHeight(15)
        self.typeLabel.setObjectName("typeLabel")
        self.typeLayout.addWidget(self.typeLabel)
        self.typeLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.typeLineEdit.setObjectName("typeLineEdit")
        self.typeLayout.addWidget(self.typeLineEdit)
        self.thirdRow.addLayout(self.typeLayout)
        self.mainLayout.addLayout(self.thirdRow)
        self.submitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.submitButton.setObjectName("submitButton")
        self.mainLayout.addWidget(self.submitButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titleLabel.setText(_translate("Form", "Add transaction"))
        self.nameLabel.setText(_translate("Form", "provide name"))
        self.priceLabel.setText(_translate("Form", "provide price"))
        self.dateLabel.setText(_translate("Form", "provide date in format: D-M-Y"))
        self.categoryLabel.setText(_translate("Form", "provide category"))
        self.typeLabel.setText(_translate("Form", "provide type"))
        self.submitButton.setText(_translate("Form", "submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_AddTransaction()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

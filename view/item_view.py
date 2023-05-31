from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QStyledItemDelegate


class TransactionDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        transaction = index.data(Qt.UserRole)
        if transaction is not None:
            font = painter.font()
            font.setBold(True)
            painter.setFont(font)
            painter.fillRect(option.rect.adjusted(0, 0, 0, 10), QColor(20, 190, 90))

            text_rect = option.rect.adjusted(0, 0, 0, 10)
            painter.drawText(text_rect, Qt.AlignTop | Qt.AlignLeft, f"Name: {transaction.name}")
            painter.drawText(text_rect, Qt.AlignTop | Qt.AlignRight, f"Price: {transaction.price}")
            painter.drawText(text_rect, Qt.AlignBottom | Qt.AlignLeft, f"Date: {transaction.date}")
            painter.drawText(text_rect, Qt.AlignBottom | Qt.AlignRight, f"Category: {transaction.category.name}")

            painter.drawLine(text_rect.left(), text_rect.bottom() + 3, text_rect.right(), text_rect.bottom() + 3)

        else:
            super().paint(painter, option, index)


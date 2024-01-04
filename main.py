import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import random


class CircleLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Добавляем сглаживание
        painter.setBrush(QColor("yellow"))
        painter.drawEllipse(self.rect())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)  # Загрузка интерфейса из файла UI.ui
        self.pushButton.clicked.connect(self.draw_circle)
        self.circle_label = CircleLabel(self.centralwidget)
        self.circle_label.setGeometry(0, 0, 0, 0)  # Изначально размеры нулевые

    def draw_circle(self):
        self.circle_label.clear()

        diameter = random.randint(50, 150)
        x = int((self.centralwidget.width() - diameter) / 2)
        y = int((self.centralwidget.height() - diameter) / 2)
        self.circle_label.setGeometry(x, y, diameter, diameter)
        self.circle_label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

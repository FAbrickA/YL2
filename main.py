from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint
from PyQt5.uic import loadUi
import sys
from random import randint


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.yellow = QColor(255, 246, 6)

        loadUi("UI.ui", self)

        self.button.clicked.connect(self.button_handler)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(self.yellow, 10, Qt.SolidLine)
        qp.setPen(pen)
        for circle in self.circles:
            x, y, d = circle
            center = QPoint(x, y)
            qp.drawEllipse(center, d, d)
        qp.end()

    def button_handler(self):
        x, y = randint(20, self.width() - 20), randint(20, self.height() - 20)
        d = randint(10, 120)
        self.circles.append((x, y, d))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    my_app = MyApp()
    my_app.show()

    sys.exit(app.exec_())

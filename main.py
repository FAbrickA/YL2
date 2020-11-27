from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint
import sys
from random import randint
from UI import Ui_MainWindow


class MyApp(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []

        self.setupUi(self)

        self.button.clicked.connect(self.button_handler)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for circle in self.circles:
            x, y, d, color = circle
            center = QPoint(x, y)
            pen = QPen(color, 10, Qt.SolidLine)
            qp.setPen(pen)
            qp.drawEllipse(center, d, d)
        qp.end()

    def button_handler(self):
        x, y = randint(20, self.width() - 20), randint(20, self.height() - 20)
        d = randint(10, 120)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.circles.append((x, y, d, color))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    my_app = MyApp()
    my_app.show()

    sys.exit(app.exec_())

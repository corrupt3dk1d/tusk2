import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn1.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawPoints(qp)
            qp.end()

    def drawPoints(self, qp):
        print(123)
        qp.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
        qp.setBrush(Qt.yellow)
        num1 = random.randint(1, 250)
        num2 = random.randint(1, 250)
        num3 = random.randint(1, 100)

        print(num1, num2)
        qp.drawEllipse(num1, num2, num3, num3)
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

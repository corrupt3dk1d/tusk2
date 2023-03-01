import sys
import random

import PyQt5.QtQuick
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from UI import Ui_MainWindow


class MyWidget(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        color = QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        qp.setPen(QPen(color, 5))
        qp.setBrush(color)
        num1 = random.randint(1, 250)
        num2 = random.randint(1, 250)
        num3 = random.randint(1, 100)

        qp.drawEllipse(num1, num2, num3, num3)
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

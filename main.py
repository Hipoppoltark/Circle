import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("UI.ui", self)
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.btn.hide()
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setPen(QColor(255, 186, 0))
        count = randint(50, 300)
        for i in range(count):
            size = randint(1, 200)
            qp.drawEllipse(randint(1, 500), randint(1, 300), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
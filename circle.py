import PyQt5.QtWidgets as QW
from PyQt5 import QtCore, QtGui, uic
from random import choice as c
from PyQt5.QtGui import QColor
import sys


class Drawer(QW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.paint = False
        uic.loadUi('form.ui', self)
        self.btn.clicked.connect(self.draw)

    def draw(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            qp = QtGui.QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            x, y = c(range(0, 630)), c(range(0, 500))
            h = c(range(40, 300))
            while not (x + h < 700 and y + h < 570):
                x, y = c(range(0, 630)), c(range(0, 500))
                h = c(range(40, 300))
            qp.drawEllipse(x, y, h, h)
            qp.end()
            self.paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QW.QApplication(sys.argv)
    ex = Drawer()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
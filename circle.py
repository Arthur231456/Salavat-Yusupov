import PyQt5.QtWidgets as QW
from PyQt5 import QtCore, QtGui, uic
from random import choice as c
from PyQt5.QtGui import QColor
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(690, 510, 101, 31))
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Желтые круги"))
        self.btn.setText(_translate("MainWindow", "Рисовать"))


class Drawer(QW.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.paint = False
        self.setupUi(self)
        self.btn.clicked.connect(self.draw)

    def draw(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            qp = QtGui.QPainter()
            qp.begin(self)
            qp.setBrush(QColor(c(range(255)), c(range(255)), c(range(255))))
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

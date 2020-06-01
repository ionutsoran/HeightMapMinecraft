# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Inner/Desktop/mapviewerUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QColor
from random import randint

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 20, 600, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label11 = QtWidgets.QLabel(self.frame)
        self.label11.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.label11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label11.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.label11.setPixmap(self.FillImageFrame())
        self.label11.setObjectName("label11")
        self.label12 = QtWidgets.QLabel(self.frame)
        self.label12.setGeometry(QtCore.QRect(300, 0, 300, 300))
        self.label12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label12.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.label12.setPixmap(self.FillImageFrame())
        self.label12.setObjectName("label12")
        self.label21 = QtWidgets.QLabel(self.frame)
        self.label21.setGeometry(QtCore.QRect(0, 300, 300, 300))
        self.label21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label21.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.label21.setPixmap(self.FillImageFrame())
        self.label21.setObjectName("label21")
        self.label22 = QtWidgets.QLabel(self.frame)
        self.label22.setGeometry(QtCore.QRect(300, 300, 300, 300))
        self.label22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label22.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.label22.setPixmap(self.FillImageFrame())
        self.label22.setObjectName("label22")
        self.label13 = QtWidgets.QLabel(self.frame)
        self.label13.setGeometry(QtCore.QRect(600, 0, 300, 300))
        self.label13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label13.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.label13.setPixmap(self.FillImageFrame())
        self.label13.setObjectName("label13")
        self.label23 = QtWidgets.QLabel(self.frame)
        self.label23.setGeometry(QtCore.QRect(600, 300, 300, 300))
        self.label23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label23.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.label23.setPixmap(self.FillImageFrame())
        self.label23.setObjectName("label23")
        self.label03 = QtWidgets.QLabel(self.frame)
        self.label03.setGeometry(QtCore.QRect(600, -300, 300, 300))
        self.label03.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label03.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label03.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.label03.setPixmap(self.FillImageFrame())
        self.label03.setObjectName("label03")
        self.label02 = QtWidgets.QLabel(self.frame)
        self.label02.setGeometry(QtCore.QRect(300, -300, 300, 300))
        self.label02.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label02.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.label02.setPixmap(self.FillImageFrame())
        self.label02.setObjectName("label02")
        self.label01 = QtWidgets.QLabel(self.frame)
        self.label01.setGeometry(QtCore.QRect(0, -300, 300, 300))
        self.label01.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label01.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.label01.setPixmap(self.FillImageFrame())
        self.label01.setObjectName("label01")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def FillImageFrame(self):
        width = 300
        height = 300
        pixmap = QPixmap(width, height)
        pixmap.fill(QColor(randint(0, 256), randint(0, 256), randint(0, 256), randint(0, 256)))

        return pixmap


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Inner/Desktop/mapviewerUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.frame11 = QtWidgets.QFrame(self.frame)
        self.frame11.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.frame11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame11.setObjectName("frame11")
        self.frame12 = QtWidgets.QFrame(self.frame)
        self.frame12.setGeometry(QtCore.QRect(300, 0, 300, 300))
        self.frame12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame12.setObjectName("frame12")
        self.frame21 = QtWidgets.QFrame(self.frame)
        self.frame21.setGeometry(QtCore.QRect(0, 300, 300, 300))
        self.frame21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame21.setObjectName("frame21")
        self.frame22 = QtWidgets.QFrame(self.frame)
        self.frame22.setGeometry(QtCore.QRect(300, 300, 300, 300))
        self.frame22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame22.setObjectName("frame22")
        self.frame13 = QtWidgets.QFrame(self.frame)
        self.frame13.setGeometry(QtCore.QRect(600, 0, 300, 300))
        self.frame13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame13.setObjectName("frame13")
        self.frame23 = QtWidgets.QFrame(self.frame)
        self.frame23.setGeometry(QtCore.QRect(600, 300, 300, 300))
        self.frame23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame23.setObjectName("frame23")
        self.frame03 = QtWidgets.QFrame(self.frame)
        self.frame03.setGeometry(QtCore.QRect(600, -300, 300, 300))
        self.frame03.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame03.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame03.setObjectName("frame03")
        self.frame02 = QtWidgets.QFrame(self.frame)
        self.frame02.setGeometry(QtCore.QRect(300, -300, 300, 300))
        self.frame02.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame02.setObjectName("frame02")
        self.frame01 = QtWidgets.QFrame(self.frame)
        self.frame01.setGeometry(QtCore.QRect(0, -300, 300, 300))
        self.frame01.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame01.setObjectName("frame01")
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

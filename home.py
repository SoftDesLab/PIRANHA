from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from pishingweb import Pishingweb
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class Ui_MainWindow(Pishingweb):

   #Events
    def homeCheck(self):

        print("Home")

    def scanning(self):
        meow = self.lineEdit.text()
        x_pred = meow.strip().split() 
        print(x_pred)
        x_pred1 = self.vectoran().fit_transform(x_pred)
        news = self.accuracy().predict(x_pred1) #ito na yung mga label kung bad/good.
        #print kung bad or good in order
        return meow

    def blacklistCheck(self):
        print("Blacklist")

    def checkerListCheck(self):
        print("Checker List")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 639)
        MainWindow.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:13px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-10, 0, 900, 620))
        self.background.setStyleSheet("background-image: url(:/background/background.jpeg);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(210, -50, 481, 221))
        self.logo.setStyleSheet("image: url(:/logo/piranhaLogo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 90, 690, 448))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background:white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.home = QtWidgets.QPushButton(self.frame)
        self.home.setGeometry(QtCore.QRect(0, 0, 230, 34))
        self.home.setAutoFillBackground(False)
        self.home.clicked.connect(self.homeCheck)
        self.home.setStyleSheet("QPushButton\n"
"{\n"
"    color:white;\n"
"    background:#333;\n"
"    border-radius:0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color:#555555;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#777777;\n"
"}")
        self.home.setObjectName("home")
        self.blacklist = QtWidgets.QPushButton(self.frame)
        self.blacklist.setGeometry(QtCore.QRect(230, 0, 230, 34))
        self.blacklist.clicked.connect(self.blacklistCheck)
        self.blacklist.setStyleSheet("QPushButton\n"
"{\n"
"    color:white;\n"
"    background:#333;\n"
"    border-radius:0px;\n"
"}"
"QPushButton:hover\n"
"{\n"
"	background-color:#555555;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#777777;\n"
"}")
        self.blacklist.setObjectName("blacklist")
        self.checkerlist = QtWidgets.QPushButton(self.frame)
        self.checkerlist.setGeometry(QtCore.QRect(460, 0, 230, 34))
        self.checkerlist.clicked.connect(self.checkerListCheck)
        self.checkerlist.setStyleSheet("QPushButton\n"
"{\n"
"    color:white;\n"
"    background:#333;\n"
"    border-radius:0px;\n"
"}"
"QPushButton:hover\n"
"{\n"
"	background-color:#555555;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#777777;\n"
"}")
        self.checkerlist.setObjectName("checkerlist")
        self.enterURL = QtWidgets.QLabel(self.frame)
        self.enterURL.setGeometry(QtCore.QRect(40, 200, 131, 19))
        self.enterURL.setStyleSheet("QLabel\n"
"{\n"
"    font-style:bold;\n"
"    color:#333;\n"
"    font-size:14px;\n"
"}")
        self.enterURL.setObjectName("enterURL")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 220, 501, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.scanning)
        self.scan = QtWidgets.QPushButton(self.frame)
        self.scan.setGeometry(QtCore.QRect(540, 220, 112, 31))
        self.scan.setAutoFillBackground(False)
        self.scan.setStyleSheet("QPushButton\n"
"{\n"
"    color:white;\n"
"    background:#0492C2;\n"
"    border-radius:0px;\n"
"}"
"QPushButton:hover\n"
"{\n"
"	background-color:#52B2BF;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	background-color:#63C5DA;\n"
"}")
        self.scan.setObjectName("scan")
        self.scan.clicked.connect(self.scanning)
        self.label = QLabel("meow")
        self.label.move(100,100)

        self.response = QtWidgets.QLabel(self.frame)
        self.response.setGeometry(QtCore.QRect(240, 260, 201, 21))
        self.response.setText("")
        self.response.setObjectName("response")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home.setText(_translate("MainWindow", "HOME"))
        self.blacklist.setText(_translate("MainWindow", "BLACKLIST"))
        self.checkerlist.setText(_translate("MainWindow", "ABOUT US"))
        self.enterURL.setText(_translate("MainWindow", "ENTER URL"))
        self.scan.setText(_translate("MainWindow", "SCAN"))
import background
import piranhaLogo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setFixedSize(890,610)
    sys.exit(app.exec_())

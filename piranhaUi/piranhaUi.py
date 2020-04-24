from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    #Events
    def homeCheck(self):
        print("Home")

    def blacklistCheck(self):
        print("Blacklist")

    def checkerListCheck(self):
        print("Checker List")

    #Main window
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 590)
        MainWindow.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:13px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color:white;\n"
"    background:black;\n"
"    border-radius:0px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 811, 531))
        self.background.setStyleSheet("background-image: url(:/background/background.jpeg);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(160, -50, 471, 211))
        self.logo.setStyleSheet("image: url(:/logo/piranhaLogo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 100, 631, 361))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background:white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        #Home button
        self.home = QtWidgets.QPushButton(self.frame)
        self.home.setGeometry(QtCore.QRect(0, 0, 211, 31))
        self.home.setObjectName("home")
        self.home.clicked.connect(self.homeCheck)

        #Blacklist button
        self.blacklist = QtWidgets.QPushButton(self.frame)
        self.blacklist.setGeometry(QtCore.QRect(210, 0, 211, 31))
        self.blacklist.setObjectName("blacklist")
        self.blacklist.clicked.connect(self.blacklistCheck)

        #Checker list button
        self.checkerlist = QtWidgets.QPushButton(self.frame)
        self.checkerlist.setGeometry(QtCore.QRect(420, 0, 211, 31))
        self.checkerlist.setObjectName("checkerlist")
        self.checkerlist.clicked.connect(self.checkerListCheck)
    
        MainWindow.setCentralWidget(self.centralwidget)
        '''
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        '''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home.setText(_translate("MainWindow", "Home"))
        self.blacklist.setText(_translate("MainWindow", "Blacklist"))
        self.checkerlist.setText(_translate("MainWindow", "Checker List"))

import background
import piranhaLogo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

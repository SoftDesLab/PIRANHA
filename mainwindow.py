# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3, background, piranhaLogo


class Ui_MainWindow(object):

    def scanCheck(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)
        url = self.lineEdit.text()
        if (url == "Bad"):
            self.label.setText(_translate("MainWindow", "STATUS: The Website is a Phishing URL."))
        else:
            self.label.setText(_translate("Mainwindow", "STATUS: The Website is not a Phishing URL,"))            
        print(url)

    def Refresh(self):
        connection = sqlite3.connect('urlData.db')
        query =  "SELECT URLs FROM URL WHERE URL.Condition='0'"
        result = connection.execute(query)
        print(result.fetchall())                
        print("Refresh")

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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(100, 90, 695, 451))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(1)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane \n"
"{ \n"
"    border-top: 2px solid white;\n"
"    position: absolute;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar \n"
"{\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab \n"
"{\n"
"    background: #333;\n"
"    min-width: 33ex;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover \n"
"{\n"
"    background: #777777;\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"      color: white;\n"
"}")
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.HomeTab = QtWidgets.QWidget()
        self.HomeTab.setObjectName("HomeTab")
        self.lineEdit = QtWidgets.QLineEdit(self.HomeTab)
        self.lineEdit.setGeometry(QtCore.QRect(40, 210, 501, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.scan = QtWidgets.QPushButton(self.HomeTab)
        self.scan.setGeometry(QtCore.QRect(540, 210, 112, 31))
        self.scan.setAutoFillBackground(False)
        self.scan.clicked.connect(self.scanCheck)
        self.scan.setStyleSheet("QPushButton\n"
"{\n"
"    color:white;\n"
"    background:#0492C2;\n"
"    border-radius:0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#52B2BF;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:#63C5DA;\n"
"}")
        self.scan.setObjectName("scan")
        self.enterURL = QtWidgets.QLabel(self.HomeTab)
        self.enterURL.setGeometry(QtCore.QRect(40, 190, 131, 19))
        self.enterURL.setStyleSheet("QLabel\n"
"{\n"
"    font-style:bold;\n"
"    color:#333;\n"
"    font-size:14px;\n"
"}")
        self.enterURL.setObjectName("enterURL")
        self.progressBar = QtWidgets.QProgressBar(self.HomeTab)
        self.progressBar.setGeometry(QtCore.QRect(40, 260, 611, 23))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"\n"
"     border-radius: 0px;\n"
"     background-color: #777777;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: #05B8CC;\n"
"     width: 20px;\n"
" }")
        # self.progressBar.setProperty("value", 35)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.HomeTab)
        self.label.setGeometry(QtCore.QRect(40, 310, 611, 20))
        self.label.setStyleSheet("font: 75 italic 10pt \"Arial\";\n"
"")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.HomeTab, "")
        self.BlackListTab = QtWidgets.QWidget()
        self.BlackListTab.setObjectName("BlackListTab")
        self.tableView = QtWidgets.QTableView(self.BlackListTab)
        self.tableView.setGeometry(QtCore.QRect(20, 50, 651, 361))
        self.tableView.setObjectName("tableView")
        self.blacklistLabel = QtWidgets.QLabel(self.BlackListTab)
        self.blacklistLabel.setGeometry(QtCore.QRect(290, 20, 121, 19))
        self.blacklistLabel.setStyleSheet("QLabel\n"
"{\n"
"    font-family:century gothic;\n"
"    color:#333;\n"
"    font-size:20px;\n"
"    \n"
"}")
        self.blacklistLabel.setIndent(-1)
        self.blacklistLabel.setObjectName("blacklistLabel")
        self.refresh = QtWidgets.QPushButton(self.BlackListTab)
        self.refresh.setGeometry(QtCore.QRect(559, 20, 112, 31))
        self.refresh.setAutoFillBackground(False)
        self.refresh.clicked.connect(self.Refresh)
        self.refresh.setStyleSheet("QPushButton\n"
"{\n"
"    color:white;\n"
"    background:#0492C2;\n"
"    border-radius:0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#52B2BF;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:#63C5DA;\n"
"}")
        self.refresh.setObjectName("refresh")
        self.tabWidget.addTab(self.BlackListTab, "")
        self.AboutUSTab = QtWidgets.QWidget()
        self.AboutUSTab.setObjectName("AboutUSTab")
        self.tabWidget.addTab(self.AboutUSTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scan.setText(_translate("MainWindow", "SCAN"))
        self.enterURL.setText(_translate("MainWindow", "ENTER URL"))
        # self.label.setText(_translate("MainWindow", "STATUS: The Website is a Phishing URL."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HomeTab), _translate("MainWindow", "HOME"))
        self.blacklistLabel.setText(_translate("MainWindow", "BLACKLIST"))
        self.refresh.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BlackListTab), _translate("MainWindow", "BLACKLIST"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AboutUSTab), _translate("MainWindow", "ABOUT US"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


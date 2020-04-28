# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.tabWidget.setGeometry(QtCore.QRect(100, 90, 673, 452))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
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
"    min-width: 28ex;\n"
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
        self.progressBar.setProperty("value", 35)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.HomeTab)
        self.label.setGeometry(QtCore.QRect(40, 310, 611, 20))
        self.label.setStyleSheet("font: 75 italic 10pt \"Arial\";\n"
"")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.HomeTab)
        self.label_6.setGeometry(QtCore.QRect(30, 90, 610, 29))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("*{\n"
"   font-family: century gothic;\n"
"   font-size: 24px;\n"
"   font-style: bold;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"  color:#333;\n"
"}")
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.HomeTab)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 631, 29))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("*{\n"
"   font-family: century gothic;\n"
"   font-size: 24px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"  color:#333;\n"
"}")
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.HomeTab)
        self.label_8.setGeometry(QtCore.QRect(490, 150, 171, 29))
        self.label_8.setStyleSheet("*{\n"
"   font-family: century gothic;\n"
"   font-size: 20px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"  color:#333;\n"
"}")
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.AboutUSTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.AboutUSTab)
        self.tabWidget_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget_2.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 0px solid #63C5DA;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"    background: white;\n"
"    min-width: 16ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #F5F5F5;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: white;\n"
"    border-bottom-color: white;\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"      color: #777777;\n"
"}")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 671, 381))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../piranhaUi/team.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, -10, 641, 401))
        self.label_5.setStyleSheet("image: url(:/team/team.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 671, 381))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../piranhaUi/about.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(-90, 0, 861, 401))
        self.label_4.setStyleSheet("image: url(:/piranhaAbout/piranha.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.AboutUSTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scan.setText(_translate("MainWindow", "SCAN"))
        self.enterURL.setText(_translate("MainWindow", "ENTER URL"))
        self.label.setText(_translate("MainWindow", "STATUS: The Website is a Phishing URL."))
        self.label_6.setText(_translate("MainWindow", "\"You\'re Judged on how you respond to an incident."))
        self.label_7.setText(_translate("MainWindow", "Early detection and quick response are key to that.\""))
        self.label_8.setText(_translate("MainWindow", "-Wayne Peterson"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HomeTab), _translate("MainWindow", "HOME"))
        self.blacklistLabel.setText(_translate("MainWindow", "BLACKLIST"))
        self.refresh.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BlackListTab), _translate("MainWindow", "BLACKLIST"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "The Team"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "PIRANHA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AboutUSTab), _translate("MainWindow", "ABOUT US"))
import background
import piranhaLogo
import piranha
import team

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#Libraries used for main.py
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from User_Interface import background, piranhaLogo, piranhaAbout, team
import sys
#Insert path of Application_Layer to run python scripts
sys.path.insert(0,"/home/paradox/Local_Repo/Project/PIRANHA/Application_Layer")
from dbmanager import Dbmanager
from data_extraction import Data_extraction

class Ui_MainWindow(object):

    #The function identifies if the entered website is a phishing website or not.
    def scanCheck(self):
        _translate = QtCore.QCoreApplication.translate
        self.completed = 0
        while self.completed < 100: #While statement is activated once the user has entered a url to show progressions.
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)
        urlInput = self.lineEdit.text()
        if urlInput != "":
            use = Data_extraction()
            status = use.prediction(urlInput)
            if status != [1]: #If statement identifies if the prediction is either from [1] - SAFE or [0] - NOT. 
                self.label.setText(_translate("MainWindow", "STATUS: THE SUSPICIOUS WEBSITE IS A PHISHING BAIT."))
            else:
                self.label.setText(_translate("Mainwindow", "STATUS: THE SUSPICIOUS WEBSITE IS NOT A PHISHING BAIT."))
        else:

            self.label.setText(_translate("Mainwindow", "STATUS: ENTER SOMETHING YOU DOUCHE."))

            self.label.setText(_translate("Mainwindow", "STATUS: The Website is not a Phishing URL."))
            print("STATUS: The Website is not a Phishing URL.")  

    #The function displays the list of phishing websites in the database.
    def Refresh(self):
        query = "SELECT URLs FROM URL WHERE URL.Condition='0'"
        use = dbmanager()
        results = use.database().execute(query)
        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(results): #For statement creates a table for the database.
            self.tableWidget.insertRow(row_num)
            for col_num, data in enumerate(row_data):    
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
        
        use.database().close()

    #The function inserts new suspicious websites to the database hence, it would increase the approximation of the program.
    def insertBL(self, insert): #Having difficulties in calling the function inputdb from db manager
        insert = self.inputBL.text()
        use = dbmanager()
        use.inputdb(insert) #Inserts the suspicious website to the database.

    #The function shows the Phishing Website analysis bargraph comparing the quantity between what is safe and not.
    def graphicBL(self):
        use = dbmanager()
        use.graphdb()

    #The function creates the interface.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") #Sets window size, and style format.
        MainWindow.resize(888, 639)
        MainWindow.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:13px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget) #Sets the main background of the program.
        self.background.setGeometry(QtCore.QRect(-10, 0, 900, 620))
        self.background.setStyleSheet("background-image: url(:/background/background.jpeg);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.logo = QtWidgets.QLabel(self.centralwidget) #Sets the logo of the program.
        self.logo.setGeometry(QtCore.QRect(200, -50, 481, 221))
        self.logo.setStyleSheet("image: url(:/logo/piranhaLogo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(100, 90, 695, 451))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(1)
        self.tabWidget.setFont(font) #Sets the Tabs from HomeTab, BlackListTab, and AboutUsTab.
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
        self.lineEdit = QtWidgets.QLineEdit(self.HomeTab) #Sets the searchbar for the scanning of suspicious website.
        self.lineEdit.setGeometry(QtCore.QRect(40, 210, 501, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("PLEASE ENTER A SUSPICIOUS WEBSITE")
        self.scan = QtWidgets.QPushButton(self.HomeTab) #Sets the button that scans the Website.
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
        self.progressBar = QtWidgets.QProgressBar(self.HomeTab) #Sets the progressBar into the GUI.
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
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.HomeTab) #Sets the output if the website is a phishing website.
        self.label.setGeometry(QtCore.QRect(40, 310, 611, 20))
        self.label.setStyleSheet("font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label.setObjectName("label")
        self.quote = QtWidgets.QLabel(self.HomeTab) #Sets an awesome quote for the program.
        self.quote.setGeometry(QtCore.QRect(38, 90, 621, 121))
        self.quote.setStyleSheet("*{\n"
"   font-family:century gothic;\n"
"   font-size:22px;\n"
"   font-weight:600;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"   color: #777777;\n"
"}")
        self.quote.setObjectName("quote")
        self.tabWidget.addTab(self.HomeTab, "")
        self.BlackListTab = QtWidgets.QWidget()
        self.BlackListTab.setObjectName("BlackListTab")
        self.refresh = QtWidgets.QPushButton(self.BlackListTab) #Sets the refresh button to show the list of phishing website.
        self.refresh.setGeometry(QtCore.QRect(30, 90, 71, 21))
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
        self.enterBL = QtWidgets.QPushButton(self.BlackListTab) #Sets the button for entering phishing website to the databse.
        self.enterBL.setGeometry(QtCore.QRect(540, 30, 112, 31))
        self.enterBL.setAutoFillBackground(False)
        self.enterBL.clicked.connect(self.insertBL)
        self.enterBL.setStyleSheet("QPushButton\n"
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
        self.enterBL.setObjectName("enterBL")
        self.inputBL = QtWidgets.QLineEdit(self.BlackListTab) #Sets the searchbar for the Phishing website to the database.
        self.inputBL.setGeometry(QtCore.QRect(30, 30, 511, 31))
        self.inputBL.setObjectName("inputBL")
        self.inputBL.setPlaceholderText("PLEASE ENTER A WEBSITE TO ADD TO BLACKLIST")
        self.Graph = QtWidgets.QPushButton(self.BlackListTab)
        self.Graph.setGeometry(QtCore.QRect(100, 90, 71, 21))
        self.Graph.setAutoFillBackground(False)
        self.Graph.setStyleSheet("QPushButton\n"
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
        self.Graph.setObjectName("Graph")
        self.Graph.clicked.connect(self.graphicBL)
        self.tableWidget = QtWidgets.QTableWidget(self.BlackListTab) #Sets the table to show the list of Phishing websites.
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 621, 291))
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setStyleSheet("font: 75 7pt \"Tahoma\";")
        self.tableWidget.setObjectName("tableWidget")
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tabWidget.addTab(self.BlackListTab, "")
        self.AboutUSTab = QtWidgets.QWidget() #Sets another section tabs in aboutUs tab
        self.AboutUSTab.setObjectName("AboutUSTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.AboutUSTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AboutTab = QtWidgets.QTabWidget(self.AboutUSTab)
        self.AboutTab.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.AboutTab.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
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
        self.AboutTab.setObjectName("abouUsTab")
        self.teamTab = QtWidgets.QWidget()
        self.teamTab.setObjectName("teamTab")
        self.teamAbout = QtWidgets.QLabel(self.teamTab) #Sets the credits to the members who build the project.
        self.teamAbout.setGeometry(QtCore.QRect(20, -10, 641, 401))
        self.teamAbout.setStyleSheet("image: url(:/team/team.jpg);")
        self.teamAbout.setText("")
        self.teamAbout.setObjectName("teamAbout")
        self.AboutTab.addTab(self.teamTab, "")
        self.abstractTab = QtWidgets.QWidget()
        self.abstractTab.setObjectName("abstractTab")
        self.piranhaAbout = QtWidgets.QLabel(self.abstractTab) #Sets the introduction on what the project is all about.
        self.piranhaAbout.setGeometry(QtCore.QRect(0, 0, 671, 381))
        self.piranhaAbout.setStyleSheet("image: url(:/piranhaAbout/piranhaAbout.jpg);")
        self.piranhaAbout.setText("")
        self.piranhaAbout.setObjectName("piranhaAbout")
        self.AboutTab.addTab(self.abstractTab, "")
        self.verticalLayout.addWidget(self.AboutTab)

        self.tabWidget.addTab(self.AboutUSTab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #The function that calls the tr() at the end of the MainWindow constructor and every time a user changes the application's language using the Language menu
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "P.I.R.A.N.H.A"))
        MainWindow.setWindowIcon(QtGui.QIcon('User_Interface/assets/iconMain.png'))
        self.scan.setText(_translate("MainWindow", "SCAN"))
        self.quote.setText(_translate("MainWindow", "<html><head/><body><p>RELENTLESS AND FIERCE AGAINST PHISHING.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.HomeTab), _translate("MainWindow", "HOME"))
        self.refresh.setText(_translate("MainWindow", "REFRESH"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "LIST OF CAPTURED PHISHING WEBSITES"))
        self.enterBL.setText(_translate("Mainwindow", "ENTER"))
        self.Graph.setText(_translate("MainWindow", "GRAPH"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BlackListTab), _translate("MainWindow", "BLACKLIST"))
        self.AboutTab.setTabText(self.AboutTab.indexOf(self.teamTab), _translate("MainWindow", "TEAM"))
        self.AboutTab.setTabText(self.AboutTab.indexOf(self.abstractTab), _translate("MainWindow", "PROJECT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AboutUSTab), _translate("MainWindow", "ABOUT US"))

#The function that executes all of the code found in the file.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# Form implementation generated from reading ui file '/home/viblab/_developments_/Projects/General_Projects/VALE_DataGUI/Desktop/DataGUI/ui/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 800)
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.grpDataPlot = QtWidgets.QGroupBox(parent=self.centralWidget)
        self.grpDataPlot.setGeometry(QtCore.QRect(10, 150, 981, 431))
        self.grpDataPlot.setStyleSheet("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } ")
        self.grpDataPlot.setObjectName("grpDataPlot")
        self.frmDataPlot = QtWidgets.QFrame(parent=self.grpDataPlot)
        self.frmDataPlot.setGeometry(QtCore.QRect(10, 20, 961, 391))
        self.frmDataPlot.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmDataPlot.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmDataPlot.setObjectName("frmDataPlot")
        self.grpDataAnalysis = QtWidgets.QGroupBox(parent=self.centralWidget)
        self.grpDataAnalysis.setGeometry(QtCore.QRect(10, 600, 981, 151))
        self.grpDataAnalysis.setStyleSheet("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } ")
        self.grpDataAnalysis.setFlat(False)
        self.grpDataAnalysis.setObjectName("grpDataAnalysis")
        self.grpAnaMethod = QtWidgets.QGroupBox(parent=self.grpDataAnalysis)
        self.grpAnaMethod.setGeometry(QtCore.QRect(9, 30, 141, 111))
        self.grpAnaMethod.setObjectName("grpAnaMethod")
        self.rbtWeibull = QtWidgets.QRadioButton(parent=self.grpAnaMethod)
        self.rbtWeibull.setGeometry(QtCore.QRect(10, 20, 89, 19))
        self.rbtWeibull.setObjectName("rbtWeibull")
        self.rbtMTTF = QtWidgets.QRadioButton(parent=self.grpAnaMethod)
        self.rbtMTTF.setGeometry(QtCore.QRect(10, 40, 89, 19))
        self.rbtMTTF.setObjectName("rbtMTTF")
        self.rbtCon = QtWidgets.QRadioButton(parent=self.grpAnaMethod)
        self.rbtCon.setGeometry(QtCore.QRect(10, 60, 111, 19))
        self.rbtCon.setObjectName("rbtCon")
        self.rbtDiawur = QtWidgets.QRadioButton(parent=self.grpAnaMethod)
        self.rbtDiawur.setGeometry(QtCore.QRect(10, 80, 111, 19))
        self.rbtDiawur.setChecked(True)
        self.rbtDiawur.setObjectName("rbtDiawur")
        self.grpAnaParams = QtWidgets.QGroupBox(parent=self.grpDataAnalysis)
        self.grpAnaParams.setGeometry(QtCore.QRect(160, 30, 481, 111))
        self.grpAnaParams.setObjectName("grpAnaParams")
        self.grpAnaResult = QtWidgets.QGroupBox(parent=self.grpDataAnalysis)
        self.grpAnaResult.setGeometry(QtCore.QRect(650, 30, 311, 111))
        self.grpAnaResult.setObjectName("grpAnaResult")
        self.grpDataSource = QtWidgets.QGroupBox(parent=self.centralWidget)
        self.grpDataSource.setGeometry(QtCore.QRect(10, 10, 831, 131))
        self.grpDataSource.setStyleSheet("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" } ")
        self.grpDataSource.setObjectName("grpDataSource")
        self.grpServerOrigin = QtWidgets.QGroupBox(parent=self.grpDataSource)
        self.grpServerOrigin.setGeometry(QtCore.QRect(10, 30, 141, 91))
        self.grpServerOrigin.setObjectName("grpServerOrigin")
        self.rbtOpenServer = QtWidgets.QRadioButton(parent=self.grpServerOrigin)
        self.rbtOpenServer.setGeometry(QtCore.QRect(20, 20, 89, 19))
        self.rbtOpenServer.setChecked(True)
        self.rbtOpenServer.setObjectName("rbtOpenServer")
        self.rbtLocalServer = QtWidgets.QRadioButton(parent=self.grpServerOrigin)
        self.rbtLocalServer.setGeometry(QtCore.QRect(20, 40, 89, 19))
        self.rbtLocalServer.setObjectName("rbtLocalServer")
        self.rbtRemoteServer = QtWidgets.QRadioButton(parent=self.grpServerOrigin)
        self.rbtRemoteServer.setGeometry(QtCore.QRect(20, 60, 89, 19))
        self.rbtRemoteServer.setObjectName("rbtRemoteServer")
        self.grpDataSet = QtWidgets.QGroupBox(parent=self.grpDataSource)
        self.grpDataSet.setGeometry(QtCore.QRect(340, 30, 271, 91))
        self.grpDataSet.setObjectName("grpDataSet")
        self.btnListDataset = QtWidgets.QPushButton(parent=self.grpDataSet)
        self.btnListDataset.setGeometry(QtCore.QRect(10, 20, 85, 27))
        self.btnListDataset.setObjectName("btnListDataset")
        self.cmbDatasetList = QtWidgets.QComboBox(parent=self.grpDataSet)
        self.cmbDatasetList.setGeometry(QtCore.QRect(100, 20, 161, 24))
        self.cmbDatasetList.setObjectName("cmbDatasetList")
        self.btnTestDataset = QtWidgets.QPushButton(parent=self.grpDataSet)
        self.btnTestDataset.setGeometry(QtCore.QRect(10, 50, 121, 27))
        self.btnTestDataset.setObjectName("btnTestDataset")
        self.btnFetchDataset = QtWidgets.QPushButton(parent=self.grpDataSet)
        self.btnFetchDataset.setGeometry(QtCore.QRect(140, 50, 121, 27))
        self.btnFetchDataset.setObjectName("btnFetchDataset")
        self.grpDataTime = QtWidgets.QGroupBox(parent=self.grpDataSource)
        self.grpDataTime.setGeometry(QtCore.QRect(160, 30, 171, 91))
        self.grpDataTime.setObjectName("grpDataTime")
        self.lblFrom = QtWidgets.QLabel(parent=self.grpDataTime)
        self.lblFrom.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.lblFrom.setObjectName("lblFrom")
        self.dateFrom = QtWidgets.QDateEdit(parent=self.grpDataTime)
        self.dateFrom.setGeometry(QtCore.QRect(50, 20, 110, 22))
        self.dateFrom.setObjectName("dateFrom")
        self.lblTo = QtWidgets.QLabel(parent=self.grpDataTime)
        self.lblTo.setGeometry(QtCore.QRect(10, 50, 21, 21))
        self.lblTo.setObjectName("lblTo")
        self.dateTo = QtWidgets.QDateEdit(parent=self.grpDataTime)
        self.dateTo.setGeometry(QtCore.QRect(50, 50, 110, 22))
        self.dateTo.setObjectName("dateTo")
        self.grpProcess = QtWidgets.QGroupBox(parent=self.grpDataSource)
        self.grpProcess.setGeometry(QtCore.QRect(620, 30, 201, 91))
        self.grpProcess.setObjectName("grpProcess")
        self.btnShowCSV = QtWidgets.QPushButton(parent=self.grpProcess)
        self.btnShowCSV.setGeometry(QtCore.QRect(10, 20, 85, 27))
        self.btnShowCSV.setObjectName("btnShowCSV")
        self.btnModifyData = QtWidgets.QPushButton(parent=self.grpProcess)
        self.btnModifyData.setGeometry(QtCore.QRect(10, 50, 85, 27))
        self.btnModifyData.setObjectName("btnModifyData")
        self.btnProcess = QtWidgets.QPushButton(parent=self.grpProcess)
        self.btnProcess.setGeometry(QtCore.QRect(100, 10, 91, 71))
        self.btnProcess.setObjectName("btnProcess")
        self.lblLogoITS = QtWidgets.QLabel(parent=self.centralWidget)
        self.lblLogoITS.setGeometry(QtCore.QRect(870, 40, 91, 81))
        self.lblLogoITS.setText("")
        self.lblLogoITS.setPixmap(QtGui.QPixmap("/home/viblab/_developments_/Projects/General_Projects/VALE_DataGUI/Desktop/DataGUI/ui/kampusmerdeka.jpg"))
        self.lblLogoITS.setScaledContents(True)
        self.lblLogoITS.setObjectName("lblLogoITS")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1099, 19))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(parent=self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAboutQt = QtGui.QAction(parent=MainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionAboutPython = QtGui.QAction(parent=MainWindow)
        self.actionAboutPython.setObjectName("actionAboutPython")
        self.actionUser_Manual = QtGui.QAction(parent=MainWindow)
        self.actionUser_Manual.setObjectName("actionUser_Manual")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuHelp.addAction(self.actionAboutPython)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grpDataPlot.setTitle(_translate("MainWindow", "Data Plot"))
        self.grpDataAnalysis.setTitle(_translate("MainWindow", "Data Analysis"))
        self.grpAnaMethod.setTitle(_translate("MainWindow", "Analysis Method"))
        self.rbtWeibull.setText(_translate("MainWindow", "Weibull"))
        self.rbtMTTF.setText(_translate("MainWindow", "MTTF"))
        self.rbtCon.setText(_translate("MainWindow", "Condition Based"))
        self.rbtDiawur.setText(_translate("MainWindow", "Diawur"))
        self.grpAnaParams.setTitle(_translate("MainWindow", "Analysis Parameters"))
        self.grpAnaResult.setTitle(_translate("MainWindow", "Analysis Results"))
        self.grpDataSource.setTitle(_translate("MainWindow", "Data Source"))
        self.grpServerOrigin.setTitle(_translate("MainWindow", "Server Origins"))
        self.rbtOpenServer.setText(_translate("MainWindow", "Open Server"))
        self.rbtLocalServer.setText(_translate("MainWindow", "Local Server"))
        self.rbtRemoteServer.setText(_translate("MainWindow", "RadioButton"))
        self.grpDataSet.setTitle(_translate("MainWindow", "Data Set"))
        self.btnListDataset.setText(_translate("MainWindow", "Refresh"))
        self.btnTestDataset.setText(_translate("MainWindow", "Test Database"))
        self.btnFetchDataset.setText(_translate("MainWindow", "Fetch Database"))
        self.grpDataTime.setTitle(_translate("MainWindow", "Data Duration"))
        self.lblFrom.setText(_translate("MainWindow", "From:"))
        self.lblTo.setText(_translate("MainWindow", "To:"))
        self.grpProcess.setTitle(_translate("MainWindow", "Process Data"))
        self.btnShowCSV.setText(_translate("MainWindow", "Show CSV"))
        self.btnModifyData.setText(_translate("MainWindow", "Modify Data"))
        self.btnProcess.setText(_translate("MainWindow", "Process"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About Team"))
        self.actionAboutQt.setText(_translate("MainWindow", "About Qt"))
        self.actionAboutPython.setText(_translate("MainWindow", "About Python"))
        self.actionUser_Manual.setText(_translate("MainWindow", "User Manual"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
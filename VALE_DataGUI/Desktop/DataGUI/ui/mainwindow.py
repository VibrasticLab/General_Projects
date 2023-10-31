# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import sys
import numpy as np

from PyQt6.QtCore import PYQT_VERSION_STR
import PyQt6.QtGui as QGui
import PyQt6.QtWidgets as QWidgets
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMessageBox

from .Ui_mainwindow import Ui_MainWindow

sys.path.append('../')
from dataprocess import DataProcess

import matplotlib
import scipy 
import pandas

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        
        self.gui_setup()
        
    def gui_setup(self):        
        dp = DataProcess()
        hbox = dp.exampleMillPlot()
        
        self.frmDataPlot.setLayout(hbox)
        
        self.statusBar.showMessage("Idle")
        self.setFixedSize(1000, 800)
        #self.showFullScreen():        
        
    @pyqtSlot()
    def on_actionAboutQt_triggered(self):
        QWidgets.QMessageBox.aboutQt(self, "About Qt")

    @pyqtSlot()
    def on_actionAboutPython_triggered(self):
        pyver = "Python: " + sys.version + "\n\n"
        npver = "NumPy: " + np.__version__ + "\n"
        qtver = "PyQt: " + PYQT_VERSION_STR + "\n"
        sciver = "SciPy: " + scipy.__version__ + "\n"
        pndver = "Pandas: " + pandas.__version__ + "\n"
        pltver = "Matplotlib: " +  matplotlib.__version__ + "\n"
        
        strversion = pyver + npver + qtver + sciver + pndver + pltver
        
        mbox = QMessageBox(self)
        mbox.setInformativeText(strversion)
        mbox.setWindowTitle("Version")
        mbox.exec()
        
    @pyqtSlot()
    def on_actionAbout_triggered(self):
        team = "Project Leader: Dr. Dhany Arifianto S.T M.Eng (dhany@ep.its.ac.id)\n"
        team += "\n"
        
        team += "Programmers:\n"
        team += "GUI Integrator: Achmadi ST MT (github.com/mekatronik-achmadi)\n"
        team += "Data Analysis : M. Ammar A. ST MT (github.com/maasyraf-project)\n"
        team += "Result Testing: A. Ainun Najib ST MT (github.com/iyyanf)\n"
        team += "Network System: Aprianto Dwi P ST MT (github.com/arkiven4)\n"
        
        mbox = QMessageBox(self)
        mbox.setInformativeText(team)
        mbox.setWindowTitle("Team List")
        mbox.setStyleSheet("QLabel{min-width: 400px;}");
        mbox.exec()
        
    @pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()        

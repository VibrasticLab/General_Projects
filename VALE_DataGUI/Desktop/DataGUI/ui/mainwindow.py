# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import sys
import numpy as np

from PyQt6.QtCore import PYQT_VERSION_STR
import PyQt6.QtWidgets as QWidgets
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMessageBox

import matplotlib

from .Ui_mainwindow import Ui_MainWindow

sys.path.append('../')
from dataprocess import DataProcess

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        
        self.gui_setup()
        
    def gui_setup(self):        
        dp = DataProcess()
        hbox = dp.examplePlot()
        
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
        npver = "NumPy: " + np.__version__ + "\n\n"
        qtver = "PyQt: " + PYQT_VERSION_STR + "\n\n"
        pltver = "Matplotlib: " +  matplotlib.__version__ + "\n\n"
        
        strversion = pyver + npver + qtver + pltver
        
        mbox = QMessageBox(self)
        mbox.setInformativeText(strversion)
        mbox.setWindowTitle("Version")
        mbox.exec()

    @pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()

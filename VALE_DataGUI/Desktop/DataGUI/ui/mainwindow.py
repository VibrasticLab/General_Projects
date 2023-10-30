# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import sys
import numpy as np

import PyQt6.QtWidgets as QWidgets
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMessageBox

from .Ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        
        self.statusBar.showMessage("Idle")
        self.showFullScreen()

    @pyqtSlot()
    def on_actionAboutQt_triggered(self):
        QWidgets.QMessageBox.aboutQt(self, "About Qt")

    @pyqtSlot()
    def on_actionAboutPython_triggered(self):
        pyver = "Python:" + sys.version + "\n\n"
        npver = "NumPy:" + np.__version__ + "\n\n"
        
        strversion = pyver + npver
        
        mbox = QMessageBox(self)
        mbox.setInformativeText(strversion)
        mbox.setWindowTitle("Version")
        mbox.exec()

    @pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()

# -*- coding: utf-8 -*-

import numpy as np

from matplotlib import style
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation	
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

import PyQt6.QtWidgets as QWidgets

import scipy.io as sio
import pandas as pd

class DataProcess():
    
    def __init__(self,  parent=None):
        pass
        
    def examplePlot(self):
        self.X = np.arange(0, 10, 0.1)
        self.Y = np.sin(self.X)
        
        self.fig = Figure(figsize=(5, 4), dpi=100, facecolor='white')
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('white')
        self.ax.grid(True,which='both',ls='-')
        self.ax.clear()
        self.line, = self.ax.plot(self.X, self.Y)
        
        style.use('ggplot')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        
        hbox = QWidgets.QHBoxLayout()
        hbox.addWidget(self.canvas)
        
        self.ani = animation.FuncAnimation(self.fig, self.graphupdate, interval=1, repeat=False,  cache_frame_data=False)
        self.ani._start()
        
        return hbox
        
    def exampleMillPlot(self):
        """
        Milling Data Source:
        https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
        """
        
        m = sio.loadmat('dataset/mill/mill.mat',struct_as_record=True)
        data = m['mill']
        l = data.dtype.names
        df_labels = pd.DataFrame()
        for i in range(7):
            # list for storing the label data for each field
            x = []
    
            # iterate through each of the unique cuts
            for j in range(167):
                x.append(data[0,j][i][0][0])
            x = np.array(x)
            df_labels[str(i)] = x

        # add column names to the dataframe
        df_labels.columns = l[0:7]
    
        # create a column with the unique cut number
        df_labels['cut_no'] = [i for i in range(167)]
        
        fig, ax = plt.subplots()

        ax.plot(data[0,166]['smcAC'],'g-',label='smcAC')
        ax.plot(data[0,166]['smcDC'],color='orange',label='smcDC')
        plt.legend()
        
        style.use('ggplot')
        self.canvas = FigureCanvas(fig)
        self.canvas.draw()
        
        hbox = QWidgets.QHBoxLayout()
        hbox.addWidget(self.canvas)
        
        return hbox

    def graphupdate(self,args):
        self.line.set_data(self.X,self.Y)

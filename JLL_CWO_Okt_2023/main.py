import numpy as np

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib import style

from extract_digiducer import extract_digiducer

if __name__ == "__main__":
    # extract digiducer data
    time, accA, accB = extract_digiducer()

    # time based plot (on progress)
    fig1 = Figure(figsize=(11,9), dpi=100, facecolor='white', tight_layout=True)
    ax1 = fig1.add_subplot(211)
    ax1.set_facecolor('white')
    ax1.grid(True,which='both',ls='-')


import numpy as np

import matplotlib.pyplot as plt
from extract_digiducer import extract_digiducer

if __name__ == "__main__":
    # extract digiducer data
    time, accA, accB = extract_digiducer()

    # time based plot (all data)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(211)
    ax1.set_facecolor('white')
    ax1.grid(True,which='both',ls='--')
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Acceleration (g)")
    line1, = ax1.plot(time, accB)

    plt.show()


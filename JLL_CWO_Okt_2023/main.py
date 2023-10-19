import numpy as np

import matplotlib.pyplot as plt
from extract_digiducer import extract_digiducer, segmenting_data

if __name__ == "__main__":
    # extract digiducer data
    time, accA, accB = extract_digiducer()

    # time based plot (all data)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.set_facecolor('white')
    ax1.grid(True,which='both',ls='--')
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Acceleration (g)")
    line1, = ax1.plot(time, accB)

    # plt.show()

    # segmenting the data
    digiducer_fs = 8000
    datapoints = [
        [0*digiducer_fs, 100*digiducer_fs],
        [100*digiducer_fs, 200*digiducer_fs],
        [200*digiducer_fs, 300*digiducer_fs],
        [300*digiducer_fs, 400*digiducer_fs],
    ]

    segmented_data = segmenting_data(accA, datapoints)

    # convert each acceleration data to velocity and displacement



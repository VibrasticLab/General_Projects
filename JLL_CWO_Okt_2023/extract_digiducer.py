import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from tkinter import filedialog as fd

def extract_digiducer():
    # define data directory
    filename = fd.askopenfilename()

    # load and setup the data
    f = pd.read_csv(filename, header=10)
    header = []
    for col in f.columns:
        header.append(col)

    # if select channel A, choose header[2], otherwise header[3]
    time = f[header[1]].to_numpy()
    accA = f[header[2]].to_numpy()
    accB = f[header[3]].to_numpy()

    print("Data extracted from selected file")

    return time, accA, accB

def segmenting_data(data, data_points):
    # create empty arary for segmented data
    segmented_data = []

    # split the data based on defined start- and end-point
    for i in range(len(data_points)):
        segment = data[data_points[i][0]:data_points[i][1]]
        segmented_data.append(segment)

    return segmented_data

def omega_arithmatic(initial_data, fs):
    # FFT parameter
    nfft = int(pow(2, np.ceil(np.log2(len(initial_data)))))
    # win = np.hamming(nfft)
    freq = (fs / 2) * np.arange(0, 1, 1/(nfft))
    amp = np.fft.fft(initial_data) #[0:int(nfft/2+1)]

    # Integration in frequency domain
    amp_int = []
    for i in range(len(amp)):
        amp_int.append(amp[i]/(2j * np.pi * freq[i]))

    converted_data = np.fft.ifft(amp_int)

    return converted_data


if __name__ == "__main__":
    extract_digiducer()

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

def omega_arithmatic(initial_data, fs, cut_off_frequency):
    # FFT parameter
    nfft = int(pow(2, np.ceil(np.log2(len(initial_data)))))
    win = np.hamming(len(initial_data))
    freq = (fs/2) * np.arange(0,1,1/(nfft/2+1))

    # Obtain FFT of initial data
    initial_spectrum = 2/len(initial_data) * np.fft.fft(win*initial_data, nfft)

    # Integration in frequency domain
    converted_spectrum = []
    for i in range(len(freq)):
        if freq[i] <= cut_off_frequency:
            converted_spectrum.append(0)
        else:
            converted_spectrum.append(initial_spectrum[i] / (2j * np.pi * freq[i]))

    converted_spectrum = np.array(converted_spectrum)

    converted_data = np.fft.ifft(converted_spectrum / (1/len(initial_data)), nfft)
    converted_data = converted_data[0:len(initial_data)]

    converted_data = converted_data / win

    return converted_data, converted_spectrum, freq
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
    segmented_data = []
    for i in range(len(data_points)):
        segment = data[data_points[i][0]:data_points[i][1]]
        segmented_data.append(segment)

    return segmented_data


if __name__ == "__main__":
    extract_digiducer()

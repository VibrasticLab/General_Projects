import numpy as np
import matplotlib.pyplot as plt
from additional_functions import *

if __name__ == "__main__":
    fs = 2000
    t = np.arange(0,0.2,(1/fs))
    nfft = int(pow(2, np.ceil(np.log2(len(t)))))
    win = np.hamming(len(t))
    freq = (fs/2) * np.arange(0,1,1/(nfft/2+1))

    acc = (10 * np.sqrt(2) * np.sin(2 * np.pi * 50 * t)
        + 5 * np.sqrt(2) * np.sin(2 * np.pi * 120 * t)
        + 8 * np.sqrt(2) * np.sin(2 * np.pi * 315 * t)
        + 2 * np.sqrt(2) * np.sin(2 * np.pi * 500 * t))

    ACC = 2/len(t) * np.fft.fft(win*acc, nfft)

    pACC = []
    for i in range(len(freq)):
        if ACC[i].imag == 0:
            pACC.append(0)
        else:
            pACC.append(np.rad2deg(np.arctan(ACC[i].real/ACC[i].imag)))
    pACC = np.array(pACC)

    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax.plot(t, acc)
    ax.grid(True, which='both')

    ax2 = fig.add_subplot(212)
    ax2.plot(freq, abs(ACC)[0:int(nfft/2+1)])
    ax2.grid(True, which='both')

    # Defining Velocity
    VEL = []
    for i in range(len(freq)):
        if freq[i] <= 20:
            VEL.append(0)
        else:
            VEL.append(ACC[i] / (2j * np.pi * freq[i]))

    VEL = np.array(VEL)

    vel = np.fft.ifft(VEL / (1/len(t)), nfft)
    vel = vel[0:len(t)]

    vel = vel / win

    fig2 = plt.figure()
    ax = fig2.add_subplot(211)
    ax.plot(freq, abs(VEL))
    ax.grid(True, which='both')

    ax2 = fig2.add_subplot(212)
    ax2.plot(t, vel)

    # Defining velosity using function in utils
    vel, VEL, freq_new = omega_arithmatic(acc, fs, cut_off_frequency=20)

    fig5 = plt.figure()
    ax = fig5.add_subplot(211)
    ax.plot(freq_new, abs(VEL)*1000)
    ax.grid(True, which='both')

    ax2 = fig5.add_subplot(212)
    ax2.plot(t, vel*1000)


    # Defining Velocity (1st approach)
    DISP = []
    for i in range(len(freq)):
        if freq[i] <= 20:
            DISP.append(0)
        else:
            DISP.append(VEL[i] / (2j * np.pi * freq[i]))

    DISP = np.array(DISP)

    disp = np.fft.ifft(DISP / (1/len(t)), nfft)
    disp = disp[0:len(t)]

    disp = disp / win

    fig4 = plt.figure()
    ax = fig4.add_subplot(211)
    ax.plot(freq, abs(DISP))
    ax.grid(True, which='both')

    ax2 = fig4.add_subplot(212)
    ax2.plot(t, disp)

    # Defining Displacement
    DISP = []
    for i in range(len(freq)):
        if freq[i] <= 20:
            DISP.append(0)
        else:
            DISP.append(ACC[i] / pow((2j * np.pi * freq[i]),2))

    DISP = np.array(DISP)

    disp = np.fft.ifft(DISP / (1/len(t)), nfft)
    disp = disp[0:len(t)]

    disp = disp / win

    fig3 = plt.figure()
    ax = fig3.add_subplot(211)
    ax.plot(freq, abs(DISP)*1e6)
    ax.grid(True, which='both')

    ax2 = fig3.add_subplot(212)
    ax2.plot(t, disp*1e6)

    plt.show()
import pyaudio
import time
import wave
import numpy as np
import matplotlib.pyplot as plt

def lowpass(sound, samplingFreq, cutoff):
    # FFT
    FFT = np.fft.fft(sound)
    # FFT Freq
    FFTfreq = np.fft.fftfreq(len(sound))*samplingFreq

    for i in range (len(FFTfreq)):
        if FFTfreq[i] > cutoff:
            FFT[i] = 0

    # Invers FFT
    IFFT = np.fft.ifft(FFT)
    return IFFT

def highpass (sound,samplingFreq,cutoff):
    # FFT
    FFT = np.fft.fft(sound)
    # FFT Freq
    FFTfreq = np.fft.fftfreq(len(sound))*samplingFreq

    for i in range (len(FFTfreq)):
        if FFTfreq[i] < cutoff:
            FFT[i] = 0

    # Invers FFT
    IFFT = np.fft.ifft(FFT)
    return IFFT
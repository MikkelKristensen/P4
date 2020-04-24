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

    for i in range(len(FFTfreq)):
        if FFTfreq[i] > cutoff:
            FFT[i] = 0


    # Invers FFT
    IFFT = np.fft.ifft(FFT)
    test = np.array(IFFT, dtype=np.int16)
    for i in range (len(test)):
        print(test[i])
    return test

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
    test = np.array(IFFT, dtype=np.int16)
    return test
import pyaudio
import time
import wave
import numpy as np
from numpy import float32
import Lowpass
import matplotlib.pyplot as plt
import sounddevice as SD

CHUNK = 4096
bufferforUnpack = CHUNK*2

ChannelIN = 1
rate = 44100

cutoff = 4000



p = pyaudio.PyAudio()

steamIN = p.open(format=pyaudio.paInt16,
                 channels=ChannelIN,
                 rate=rate,
                 input=True,
                 frames_per_buffer=CHUNK,
                )



steamOUT = p.open(format=pyaudio.paInt16,
                  channels=1,
                  rate=rate,
                  output=True)

steamIN.start_stream()

def liveRecording(steamIn, num):
    data = steamIn.read(CHUNK, exception_on_overflow=False)
    waveData = wave.struct.unpack("%dh"%(CHUNK), data)
    npArrayData = np.array(waveData)
    samples = npArrayData.astype(np.int16).tostring()

    if num == 0:
        return samples
    elif num == 1:
        return npArrayData
    elif num == 2:
        return waveData
    elif num == 3:
        return data



while steamIN.is_active():
    Rec = liveRecording(steamIN, 1)

    lowFreq = Lowpass.lowpass(Rec, CHUNK, cutoff)
    bandpass = Lowpass.highpass(lowFreq, CHUNK, -cutoff)

    npA = np.array(bandpass)
    playable = npA.real.astype(np.int16).tostring()
    steamOUT.write(playable)


    # data = steamIN.read(CHUNK, exception_on_overflow=False)
    # waveData = wave.struct.unpack("%dh"%(CHUNK), data)
    # npArrayData = np.array(waveData)
    # samples = npArrayData.astype(np.int16).tostring()
    # steamOUT.write(samples)



steamIN.stop_stream()
steamIN.close()
p.terminate()



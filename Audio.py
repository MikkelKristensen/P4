import pyaudio
import wave
import struct
import wavio
import time
import numpy as np
from matplotlib import pyplot as plt
import letsplotit

def read_whole(wavefile):
    ret = []
    while wavefile.tell() < wavefile.getnframes():
        try:
            decoded = struct.unpack("<hh", wavefile.readframes(1))
            ret.append(decoded)
        except Exception as e:
            print(e)
    return ret

def make_delay(array, framerate, delayTime, iterations, strength):
    iterations += 1
    length = len(array)
    delayedTime = int(delayTime * iterations * framerate)
    delayTimer = int(delayTime * framerate)
    newshape = (len(array) + delayedTime, 2)
    d_array = np.zeros(newshape)
    for i in range(0, length):
        d_array[i] = array[i]
    for i in range(1, iterations + 1):
        delayPoint = i * delayTimer
        for j in range(0, length):
            d_array[j + delayPoint] += ((array[j] * strength) * ((iterations - i) / iterations))

    return d_array

def playSans(sansy):
    wf = wave.open('Sans.wav', 'rb')
    p = pyaudio.PyAudio()


    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    xdnp = make_delay(np.copy(read_whole(wf)), wf.getframerate(), 1, sansy*2, 0.8)

    #lav plot aka Hollywood maskine
    #letsplotit.plotit(xdnp)

    print("Playing sans undertale")
    #Play dat shit
    stream.write((xdnp.astype(np.int16).tostring()))

    stream.close()
    wf.close()

    # close PyAudio (7)
    p.terminate()
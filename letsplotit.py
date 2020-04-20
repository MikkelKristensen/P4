import matplotlib.pyplot as plot
import numpy as np

startpunkt = 20000
samplelangt = 100

def plotit(xdnp):
    # Get x values of the sine wave

    tid = np.empty(int(len(xdnp)))
    for i in range(0, int(len(xdnp))):
        tid[i] = i

    # tid2 = np.empty(100)
    # for i in range(startpunkt, startpunkt + samplelangt):
    #     tid2[i-startpunkt] = tid[startpunkt+i]

    # Amplitude of the sine wave is sine of a variable like time

    amplitude = np.empty(int(len(xdnp)))
    for i in range(0, int(len(xdnp))):
        amplitude[i] = xdnp[i][0]

    # amplitude2 = np.empty(100)
    # for i in range(startpunkt, startpunkt + samplelangt):
    #     amplitude2[i-startpunkt] = amplitude[startpunkt+i]

    # Plot a sine wave using time and amplitude obtained for the sine wave

    plot.plot(tid, amplitude)

    # Give a title for the sine wave plot

    plot.title('Sine wave')

    # Give x axis label for the sine wave plot

    plot.xlabel('Time')

    # Give y axis label for the sine wave plot

    plot.ylabel('Amplitude = sin(time)')

    plot.grid(True, which='both')

    plot.axhline(y=0, color='k')  # Adds a line at y=0

    plot.show()

    # Display the sine wave

    plot.show()
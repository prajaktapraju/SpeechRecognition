import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# read the input audio file
sampling_freq, signal =wavfile.read('C:\\Users\\prajk\\OneDrive\\Desktop\\my project\\SpeechRecog\\Welcome.wav')

# print the shape of the signal, datatype and duration of the audo signals
print('\n Signal Shape:', signal.shape)
print('Datatype:', signal.dtype)
print('Signal duration:', round(signal.shape[0] / float(sampling_freq), 2), 'seconds')

# Normalize the signals
signal = signal / np.power(2, 15)

# extract
signal = signal[:50]

# construct the time axis
time_axis = 1000 * np.arange(0, len(signal), 1 ) / float(sampling_freq)

# plo the audio signal
plt.plot(time_axis, signal, color = 'green')
plt.xlabel('Time(miliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')
plt.show()



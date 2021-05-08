import numpy  as np
import matplotlib.pyplot as plt
from scipy.io import wavfile 
import signal as signal
# read stored audio files
# SciPy is used for numpy (for all scientific mathematical problems)
# path of stored wav file
frequency_sampling, audio_signal = wavfile.read("C:\\Users\\prajk\\OneDrive\\Desktop\\my project\\SpeechRecog\\Welcome.wav")

print('\n Signal shape:', audio_signal.shape)
print('Signal Datatype:', audio_signal.dtype)
print('Signal duration:', round(audio_signal.shape[0] / float(frequency_sampling), 2), 'seconds')

# # # normalize the signal 
audio_signal = audio_signal / np.power(2, 15)
audio_signal = audio_signal[:100]
time_axis = 100 * np.arange(0, len(signal), 1) / float(frequency_sampling)

# # # visualize the signal ussing commands
plt.plot(time_axis, color = 'blue')
plt.xlabel('Time (miliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')
plt.show()
# -------------------------Characterizing audio signal ---------------(convert audio signal time domain to frequency domain)--------------------------------------------------

# frequency_sampling, audio_signal = wavfile.read("C:\\Users\\prajk\\OneDrive\\Desktop\\my project\\SpeechRecog\\Welcome.wav")
# print('\n Signal Shape:', audio_signal.shape)
# print('Signal Datatype:', audio_signal.dtype)
# print('Signal duration:', round(audio_signal.shape[0] / float(frequency_sampling), 2,), 'seconds')
# audio_signal = audio_signal/np.power(2, 15)
# length_signal = len(audio_signal)
# half_length = np.ceil((length_signal + 1) / 2.0).astype(np.int64)
# signal_frequency = np.fft.fft(audio_signal)
# signal_frequency = abs(signal_frequency[0:half_length]) / length_signal
# signal_frequency **= 2

# len_fts = len(signal_frequency)


# if length_signal % 2:
#     signal_frequency[1: len_fts] *= 2
# else:
#     signal_frequency[1: len_fts] *=2

# signal_power = 10 * np.log10(signal_frequency)

# x_axis = np.arange(0, half_length, 1) * (frequency_sampling / length_signal)/1000.0

# plt.figure()
# plt.plot(x_axis, signal_power, color= 'black')
# plt.xlabel('Frequency(kHz)')
# plt.ylabel('Signal power (dB)')
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# out put file where the audio will bs saved
output_file=  'C:\\Users\\prajk\\OneDrive\\Desktop\\my project\\SpeechRecog\\Welcome.wav'

# specify the audio parameters
duration = 5
sampling_freq = 44100
tone_freq = 784
min_val = -5 * np.pi
max_val = 5 * np.pi

# generating audio signal using the defined parameters:
 
t = np.linspace(min_val, max_val, duration * sampling_freq)
signal = np.sin(2 * np.pi * tone_freq * t)

# add some noise to the signal
noise = 0.8 * np.random.rand(duration * sampling_freq)
signal += noise

# Normalize the scale in the output file:
# scale it ti 16 bit interger values
scaling_factor = np.power(2, 16) - 1
signal_normalized = signal / np.max(np.abs(signal))
signal_scaled = np.int16(signal_normalized * scaling_factor)

# save the generated audio signals in the output files
write(output_file, sampling_freq, signal_scaled)

# extract the first 200 values for plotting:
signal = signal[:200]

# construct the time axis in milliseconds\

time_axis = 1000 * np.arange(0, len(signal), 1) / float(sampling_freq)

# plot the audio signal
plt.plot(time_axis, signal, color = 'blue')
plt.xlabel('Time (miliseconds)')
plt.ylabel('Amplitude')
plt.title('Generted audio signal')
plt.show()

# generating audio signals using defined parameters is also called as generating monotone signals

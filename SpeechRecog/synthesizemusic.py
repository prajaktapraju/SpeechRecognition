import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import html5lib

# define a function to a generate a tone bases on the input parameters:

def tone_synthesizer(freq, duration, amplitude = 1.0, sampling_freq = 44100):
    time_axis = np.linespace(0, duration, duration * sampling_freq)
    signal = amplitude * np.sin(2 * np.pi * freq * time_axis)
    return signal.astype(np.int16)

# construct the audio signal using the parameters specific and return it:
if __name__ == '__main__':
    file_tone_single = 'generated_tone_single.wav'
    file_tone_sequence = 'generated_tone_sequence.wav'

# using a tone mapping file that contains the mapping from tone names

# mapping_file = "https://pages.mtu.edu/~suits/notefreqs.html"
mapping_file = 'tone_mapping.json'
with open(mapping_file, 'r') as f:
    tone_map = json.loads(f.read())

# lets generate the F tone with duration of 3 seconds:

tone_name = 'F'
duration = 3
amplitude = 12000
sampling_freq = 44100     

# extract the corresponding tone frequency

tone_freq =  tone_map[tone_name]

# generate the tone using the tone synthesizer function

synthesized_tone = tone_synthesizer(tone_freq, duration, amplitude, sampling_freq)

# lets generate a tone squence to make it sound like music. lets efine a tone squence with corresponding duration in seconds:
tone_sequence = [('G', 0.4),('D', 0.5),('F', 0.3), ('C', 0.6), ('A', 0.4)]

# construct the audio signal based on the squence
signal = np.array([])
for item in tone_sequence:
    tone_name = item[0]

# for each tone, extrct the corresponding frequency    # 
freq = tone_map[tone_name]

# extract the corresponding duration
duration = item[1]

# sythesize the tone using the tone sythesizer function:
synthesized_tone = tone_synthesizer(freq, duration, amplitude, sampling_freq)

# append it to the main o/p signal
signal = np.append(signal, synthesized_tone, axis=0)

# save the main o/p signal to the o/p file
write(file_tone_sequence, sampling_freq, signal)
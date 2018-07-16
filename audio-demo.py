# set up wave parameters
tone_frequency = 440
tone_amplitude = 0.5
tone_duration = 4
samplerate = 48000 # Sample period T = 1/samplerate
print ("One digital audio sample lasts just {:.10f} seconds!".format(1/samplerate))

# set up timeline for each sample
import numpy as np
total_samples = tone_duration*samplerate+1
print ("We'll generate {} total samples".format(total_samples))
t = np.linspace(0, tone_duration, total_samples)
print("Our list of sample times: {}".format(t))

# generate the wave!
wave = tone_amplitude * np.sin( 2 * np.pi * tone_frequency * t)

# this function helps visualize audio - check out utils.py
from utils import view_audio

view_audio(wave, samplerate, min_sample=0, max_sample=2048)

# generate and view a chirp signal
start_freq = 4  # This might be below human hearing, but it helps to visualize in the plot below
end_freq = 8000 # If you go too high the chirp will get painful to listen to towards the end!
freq_sweep = np.logspace(np.log2(start_freq), np.log2(end_freq), num=total_samples, base=2)
chirp_wave = tone_amplitude * np.sin( np.cumsum(2 * np.pi * freq_sweep/samplerate))
view_audio(chirp_wave, samplerate)
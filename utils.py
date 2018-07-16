# A function for visualizing audio samples and the spectrogram
def view_audio(audio, Fs, min_sample=0, max_sample=-1):
    
    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    rcParams.update({'font.size': 20})
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10))
    plt.subplots_adjust(hspace=0.37, top=0.95, bottom=0.1)
    plot_audio = audio[min_sample:max_sample].squeeze()
    ax1.plot(plot_audio, '.', ms='2')
    ax1.set_title('Audio Samples')
    ax1.set_xlabel('Sample number'); ax1.set_ylabel('Sample amplitude')
    
    ax2.specgram(plot_audio, NFFT=1024, Fs=Fs, noverlap=256);
    ax2.set_yscale('log')
    ax2.set_ylim(10,20000)
    ax2.set_title('Spectrogram')
    ax2.set_xlabel('Time (sec)'); ax2.set_ylabel('Frequency (Hz)')

    plt.show()
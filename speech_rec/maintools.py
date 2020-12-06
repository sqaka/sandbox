import wave as wave
import pyroomacoustics as pa
import scipy.signal as sp
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

import click


N_SAMPLE = 40000
SAMPLE_RATE = 16000
SAVE_DIR = './data/'


def play_sound(data, wav):
    sd.play(data, wav.getframerate())
    print('Now playing...')
    sd.wait()


def delete_db(stft_data):
    stft_data[100:, :] = 0
    return stft_data


def open_wav_file(fname):
    save_dir = SAVE_DIR
    wav = wave.open('{}{}'.format(save_dir, fname))

    print('Sampling Hz [Hz]: ', wav.getframerate())
    print('Sample size [Byte]: ', wav.getsampwidth())
    print('Sample Number: ', wav.getnframes())
    print('Channel Number: ', wav.getnchannels())

    data = wav.readframes(wav.getnframes())
    data = np.frombuffer(data, dtype=np.int16)
    wav.close()

    return wav, data


def make_graph(wav, data):
    data = data / np.iinfo(np.int16).max
    x = np.array(range(wav.getnframes())) / wav.getframerate()
    plt.figure(figsize=(10, 4))
    plt.xlabel('Time [sec]')
    plt.ylabel('Value [-1, 1]')
    plt.plot(x, data)

    plt.savefig('./wave_form.png')
    plt.show()


def fourier(data, wav):
    f, t, stft_data = sp.stft(data, fs=wav.getframerate(),
                              window='hann', nperseg=512, noverlap=256)
    print('shape: ', np.shape(stft_data))
    print('Hz: ', f)
    print('sec: ', t)

    return f, t, stft_data


def make_fourier_graph(stft_data, wav):
    fig = plt.figure(figsize=(10, 4))
    spectrum, freqs, t, im = plt.specgram(stft_data, NFFT=512, noverlap=512/16*15,
                                          Fs=wav.getframerate())
    fig.colorbar(im).set_label('Intensity [dB]')
    plt.xlabel('Time [sec]')
    plt.ylabel('Frequency [Hz]')

    plt.savefig('./spectrogram.png')
    plt.show()


def refourier(stft_data, wav):
    stft_data = delete_db(stft_data)
    t, data_post = sp.istft(stft_data, fs=wav.getframerate(),
                            window='hann', nperseg=512, noverlap=256)
    data_post = data_post.astype(np.int16)

    play_sound(data_post, wav)

    save_dir = SAVE_DIR
    rf_fname = 'istft_post_wave.wav'
    wave_out = wave.open('{}{}'.format(save_dir, rf_fname), 'w')
    wave_out.setnchannels(1)
    wave_out.setsampwidth(2)
    wave_out.setframerate(wav.getframerate())
    wave_out.writeframes(data_post)

    wave_out.close()
    wav.close()

    return rf_fname


def cut_noise(rf_fname, t):
    speech_signal, n_speech = open_wav_file(rf_fname)
    n_speech = wave.open('{}{}'.format(SAVE_DIR, rf_fname)).getnframes()
    n_noise_only = N_SAMPLE
    sampling_rate = SAMPLE_RATE
    n_sample = n_noise_only + n_speech

    wgn_signal = np.random.normal(scale=0.04, size=n_sample)
    wgn_signal = wgn_signal * np.iinfo(np.int16).max
    wgn_signal = wgn_signal.astype(np.int16)

    mix_signal = wgn_signal
    mix_signal[n_noise_only:] += speech_signal
    sftf_data = fourier(mix_signal, speech_signal)

    amp = np.abs(sftf_data)
    phase = sftf_data / np.maximum(amp, 1.e-20)
    n_noise_only_frame = np.sum(t < (n_noise_only/sampling_rate))

    p = 1.0
    alpha = 2.0
    noise_amp = np.power(np.mean(np.power(amp, p)[:, :n_noise_only_frame],
                                 axis=1, keepdims=True), 1./2)
    eps = 0.01 * np.power(amp, p)
    processed_amp = np.power(np.maximum(np.power(amp, p)-alpha*np.power(noise_amp, p), eps), 1./p)
    processed_stft_data = processed_amp * phase
    t, processed_data_post = sp.istft(processed_stft_data, fs=speech_signal.getframerate(),
                                      window='hann', nperseg=512, noverlap=256)
    # return t, processed_data_post
    make_fourier_graph(processed_stft_data, n_speech)


@click.command()
@click.option('-f', '--fname', default='arctic_a0001.wav')
def main(fname):
    wav, data = open_wav_file(fname)
    make_graph(wav, data)
    f, t, stft_data = fourier(data, wav)
    make_fourier_graph(stft_data, wav)
    rf_fname = refourier(stft_data, wav)
    cut_noise(rf_fname, t)

if __name__ == '__main__':
    main()

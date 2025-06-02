from pydub.generators import Sine
from pydub import AudioSegment
from numpy.fft import irfft
import numpy as np

AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"  

duration_ms = 10 * 60 * 1000  # 10 minutos
sample_rate = 44100

def generateBinaural(duration_ms, reddbOverlay): #Ruido de 40hz Simulado 
    left_freq = 440  # Hz
    right_freq = 480  # Hz
    left_tone = Sine(left_freq).to_audio_segment(duration=duration_ms).pan(-1)
    right_tone = Sine(right_freq).to_audio_segment(duration=duration_ms).pan(1)
    return left_tone.overlay(right_tone) - reddbOverlay

def generate_pink_noise(duration_ms, sample_rate=44100): #Ruido Rosa
    n_samples = int((duration_ms / 1000) * sample_rate)
    uneven = n_samples % 2
    X = np.random.randn(n_samples // 2 + 1 + uneven) + 1j * np.random.randn(n_samples // 2 + 1 + uneven)
    S = np.sqrt(np.arange(len(X)) + 1.)
    y = irfft(X / S).real
    y = y / np.max(np.abs(y))  # Normaliza
    audio = (y * 32767).astype(np.int16).tobytes()
    return AudioSegment(data=audio, sample_width=2, frame_rate=sample_rate, channels=1)

binaural = generateBinaural(duration_ms, -10)
pink_noise = generate_pink_noise(duration_ms).set_channels(2)
binaural_with_pink = binaural.overlay(pink_noise - 8) -10 # ruído rosa mais baixo

output_path = r"binaural_40hz_10min_pink_noise.wav"
binaural_with_pink.export(output_path, format="wav")

print(f"✅ Arquivo gerado com sucesso: {output_path}")

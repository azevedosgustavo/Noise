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

binaural = generateBinaural(duration_ms, -10)


output_path = r"binaural_40hz_10min.wav"
binaural.export(output_path, format="wav")

print(f"✅ Arquivo gerado com sucesso: {output_path}")

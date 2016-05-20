# -*- coding: utf-8 -*-

import librosa

def wave_to_chromagram(audio_path):
    y, sr = librosa.load(audio_path)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    C = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)
    return C, sr

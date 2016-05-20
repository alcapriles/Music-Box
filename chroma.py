# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import librosa
import seaborn
seaborn.set(style='ticks')
import chroma_wave

def make_chroma():
    audio_path = "background.wav"
    C, sr = chroma_wave.wave_to_chromagram(audio_path)
    
    # Make a new figure
    plt.figure(figsize=(12,4))
    
    # Display the chromagram: the energy in each chromatic pitch class as a function of time
    # To make sure that the colors span the full range of chroma values, set vmin and vmax
    librosa.display.specshow(C, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
    
    
    plt.title('Chromagram')
    plt.colorbar()
    
    plt.tight_layout()
    
    plt.show()
    return C

C = make_chroma()

def find_notes2(C):
    colunas = len(C[1,:])
    nots = ['z']
    for j in range(colunas):
        for i in range(12):
            if (C[i,j] > 0.9) and (C[i,j] != C[i,j-1]):
                if i == 0:
                    nots.append('c ')
                elif i == 1:
                    nots.append('cis ')
                elif i == 2:
                    nots.append('d ')
                elif i == 3:
                    nots.append('dis ')
                elif i == 4:
                    nots.append('e ')
                elif i == 5:
                    nots.append('f ')
                elif i == 6:
                    nots.append('fis ')
                elif i == 7:
                    nots.append('g ')
                elif i == 8:
                    nots.append('gis ')
                elif i == 9:
                    nots.append('a ')
                elif i == 10:
                    nots.append('ais ')
                elif i == 11:
                    nots.append('b ')
    nots.remove('z')
    return nots

def make_input(L):
    notas = """\\relative c' {\n"""
    for i in L:
        notas += i
    notas += """\n}"""
    return notas

def save_lilypond(notas):
#    arquivo = open('teste.ly', 'w')
#    arquivo.writelines(notas)
#    arquivo.close()
    
    with open('teste.ly', 'w') as f:
        f.writelines(notas)

a = find_notes2(C)
print (a)

b = make_input(a)
print(b)

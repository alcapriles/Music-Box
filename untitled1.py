# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import librosa
import seaborn
seaborn.set(style='ticks')
import chroma_wave

audio_path = "scale.wav"
C, sr = chroma_wave.wave_to_chromagram(audio_path)

# Make a new figure
plt.figure(figsize=(12,4))

# Display the chromagram: the energy in each chromatic pitch class as a function of time
# To make sure that the colors span the full range of chroma values, set vmin and vmax
librosa.display.specshow(C, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)

print(C)
print(len(C[:,1]))

plt.title('Chromagram')
plt.colorbar()

plt.tight_layout()

plt.show()

def find_notes2(C):
    colunas = len(C[1,:])
    nots = ['z']
    for j in range(colunas):
        for i in range(12):
            if (C[i,j] > 0.9) and (C[i,j] != C[i-1,j]):
                nots.append(i)
    return nots

a = find_notes2(C)
print (a)

                


def find_notes(C):    
    colunas = len(C[1,:])
    notas = """\\relative c' {\n"""
    for j in range(colunas):
        for i in range(12):
            if C[i,j] > 0.9:
                if i == 0:
                    notas += 'b '
                    
                elif i == 1:
                    notas += 'ais '
                    
                elif i == 2:
                    notas += 'a '
                    
                elif i == 3:
                    notas += 'gis '
                    
                elif i == 4:
                    notas += 'g '
                    
                elif i == 5:
                    notas += 'fis '
                    
                elif i == 6:
                    notas += 'f '
                    
                elif i == 7:
                    notas += 'e '
                    
                elif i == 8:
                    notas += 'dis '
                    
                elif i == 9:
                    notas += 'd '
                    
                elif i == 10:
                    notas += 'cis '
                    
                elif i == 11:
                    notas += 'c '
    
    notas += """\n}"""
    return notas

n = find_notes(C)

print(n)

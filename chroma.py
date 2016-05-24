# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import librosa
import seaborn
seaborn.set(style='ticks')
import chroma_wave
from itertools import groupby

def make_chroma():
    audio_path = "scale.wav"
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
print(len(C[1,:]))

def find_notes2(C):
    colunas = len(C[1,:])
    nots = dict()
    #notes = ['c ', 'cis ', 'd ','dis ' ,'e ' ,'f ' ,'fis ' ,'g ' ,'gis ' ,'a ' ,'ais ','b ']
    for i in range(12):
        for j in range(colunas):
            if C[i,j] > 0.9:
                if i == 0:
                    if j in dict.keys(nots):
                        nots[j].append('c ')
                    else:
                        nots[j] = ['c ']
                elif i == 1:
                    if j in dict.keys(nots):
                        nots[j].append('cis ')
                    else:
                        nots[j] = ['cis ']
                elif i == 2:
                    if j in dict.keys(nots):
                        nots[j].append('d ')
                    else:
                        nots[j] = ['d ']
                elif i == 3:
                    if j in dict.keys(nots):
                        nots[j].append('dis ')
                    else:
                        nots[j] = ['dis ']
                elif i == 4:
                    if j in dict.keys(nots):
                        nots[j].append('e ')
                    else:
                        nots[j] = ['e ']
                elif i == 5:
                    if j in dict.keys(nots):
                        nots[j].append('f ')
                    else:
                        nots[j] = ['f ']
                elif i == 6:
                    if j in dict.keys(nots):
                        nots[j].append('fis ')
                    else:
                        nots[j] = ['fis ']
                elif i == 7:
                    if j in dict.keys(nots):
                        nots[j].append('g ')
                    else:
                        nots[j] = ['g ']
                elif i == 8:
                    if j in dict.keys(nots):
                        nots[j].append('gis ')
                    else:
                        nots[j] = ['gis ']
                elif i == 9:
                    if j in dict.keys(nots):
                        nots[j].append('a ')
                    else:
                        nots[j] = ['a ']
                elif i == 10:
                    if j in dict.keys(nots):
                        nots[j].append('ais ')
                    else:
                        nots[j] = ['ais ']
                elif i == 11:
                    if j in dict.keys(nots):
                        nots[j].append('b ')
                    else:
                        nots[j] = ['b ']
    return nots

nots = find_notes2(C)
print(nots)


for k, g in groupby(sorted(nots),
                    key=nots.get):
    print('{}: {}'.format(list(g)[-1], k))

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





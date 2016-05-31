import numpy as np
import matplotlib.pyplot as plt
import librosa
import seaborn
seaborn.set(style='ticks')
from itertools import groupby
import json

def wave_to_chromagram(audio_path):
    y, sr = librosa.load(audio_path)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    C = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)
    return C, sr

def make_chroma(path):
    audio_path = path
    
    C, sr = wave_to_chromagram(audio_path)
    
#    plt.figure(figsize=(12,4))
#    librosa.display.specshow(C, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
#    plt.title('Chromagram')
#    plt.colorbar()
#    plt.tight_layout()
#    plt.show()
    
    return C

def find_notes2(C):
    colunas = len(C[1,:])
    nots = dict()
    for i in range(12):
        for j in range(colunas):
            if C[i,j] == 1.0:
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
    print(nots)
    return nots

def update_notes(nots):
    updated_nots = []
    for k, g in groupby(sorted(nots),
                        key=nots.get):
        updated_nots.append('"{}": {}'.format(list(g)[-1], json.dumps(k)))
    print(updated_nots)    
    return updated_nots
    


def remake_dict(updated_nots):
    s = ",".join(updated_nots)
    s = "{" + s + "}"
    d = json.loads(s)
    print(d)
    return d

def make_input(d):
    the_end = """\\relative c' {\n"""
    
    sorted_notes = sorted(list(d.items()), key=lambda item: int(item[0]))
    print("sorted_notes: {0}".format(sorted_notes))
    for i in sorted_notes:
        if len(i[1]) == 1:        
            the_end += i[1][0]
        elif len(i[1]) > 1:
            the_end += '<'
            for j in range(len(i[1])):
                the_end += i[1][j]
            the_end += '>'
    the_end += """\n}"""
    print(the_end)
    return the_end

def save_lilypond(the_end):
    with open('teste.ly', 'w') as f:
        f.writelines(the_end)



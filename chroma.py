import numpy as np
import matplotlib.pyplot as plt
import librosa
import seaborn
seaborn.set(style='ticks')
import chroma_wave
from itertools import groupby
import json

def make_chroma():
    audio_path = "background.wav"
    
    C, sr = chroma_wave.wave_to_chromagram(audio_path)
    
    plt.figure(figsize=(12,4))
    librosa.display.specshow(C, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
    plt.title('Chromagram')
    plt.colorbar()
    plt.tight_layout()
    plt.show()
    
    return C

C = make_chroma()

def find_notes2(C):
    colunas = len(C[1,:])
    nots = dict()
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
print('nots: (this dict contais the pairs: time: pitch)')
print(nots)

def update_notes(nots):
    updated_nots = []
    for k, g in groupby(sorted(nots),
                        key=nots.get):
        updated_nots.append('"{}": {}'.format(list(g)[-1], json.dumps(k)))
    return updated_nots

updated_nots = update_notes(nots)
print('updated_nots: (nots extracted from the giant dictionary)')
print(updated_nots)

def remake_dict(updated_nots):
    s = ",".join(updated_nots)
    s = "{" + s + "}"
    d = json.loads(s)
    return d

d = remake_dict(updated_nots)
print('remade dictionary: (in order to get the nots only by accessing the values)')
print(d)

'''
the_end = ''
for key,value in d.items():
    the_end += value[0]
    '''

def make_input(d):
    the_end = """\\relative c' {\n"""
    for key,value in d.items():
        if (value[0] == 'c ') or (value[0] == 'cis ') or (value[0] == 'd ') or (value[0] == 'dis ') or (value[0] == 'e ') or (value[0] == 'f ') or (value[0] == 'fis ') or (value[0] == 'g ') or (value[0] == 'gis ') or (value[0] == 'a ') or (value[0] == 'ais ') or (value[0] == 'b '):        
            the_end += value[0]
        else:
            the_end += '<' + value[0] + '>'
    the_end += """\n}"""
    return the_end

the_end = make_input(d)
print('the_end:')
print(the_end)
print('c cis d dis e f fis g gis a ais b')

def save_lilypond(the_end):
    with open('teste.ly', 'w') as f:
        f.writelines(the_end)





import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sg
import math
import wave
import pylab
import operator

Nfft=2048
A5=880
nbin=12
st=2**(1/float(nbin))
step=128
fr=11025
df=4
    
colunas = len(CS[1,:])
notas = "\\relative c' { "
for j in range(colunas):
    a = []
      
    for i in range(12):
        if CS[i,j] > 0.95:
            if i == 0:
                a.append('b')
                
            elif i == 1:
                a.append('a-sharp')
                
            elif i == 2:
                a.append('a')
                
            elif i == 3:
                a.append('g-sharp ')
                
            elif i == 4:
                a.append('g ')
                
            elif i == 5:
                a.append('f-sharp ')
                
            elif i == 6:
                a.append('f ')
                
            elif i == 7:
                a.append('e ')
                
            elif i == 8:
                a.append('d-sharp ')
                
            elif i == 9:
                a.append('d ')
                
            elif i == 10:
                a.append('c-sharp ')
                
            elif i == 11:
                a.append('c ')
                
        if len(a) >= 3:
            for u in range (len(a)-1):
                if len(a) == 3:
                    notas += '<<{} {} {}>>'.format(a[0], a[1], a[2])
                if len(a) == 4:
                    notas+= '<<{} {} {} {}>>'.format(a[0], a[1], a[2], a[3])
                if len(a) == 5:
                    notas+= '<<{} {} {} {} {}>>'.format(a[0], a[1], a[2], a[3], a[4])
                if len(a) == 6:
                    notas+= '<<{} {} {} {} {} {}>>'.format(a[0], a[1], a[2], a[3], a[4], a[5])
                            
                            
            else:
                for v in range (len(b)-1):
                    notas+= a[v]
notas += '}'
#O programa varre primeiro as colunas da matriz, e para cada linha da coluna selecionada observa-se se possui notas relevantes.
#A partir disso, verifica-se a presença de acordes, e os adiciona, ou não, na string.
        
tunechroma1=[np.log2(A5*st**i) for i in range(nbin)] 
tunechroma2=[int(np.log2(A5*st**i)) for i in range(nbin)]
chroma=np.asarray(tunechroma1)-np.asarray(tunechroma2);

spf = wave.open('output.wav','r')

signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

b = sg.firwin(30, 1.0/df)
signal = sg.lfilter(b, 1., signal)
signal = signal.swapaxes(0,-1)[30+1::4].swapaxes(0,-1)

fs = fs / df

step=Nfft-step

Pxx, freqs, bins, im  = pylab.specgram(signal,Fs=fs,window=np.hamming(Nfft),NFFT=Nfft,noverlap=step,Fc=0)

freqs = freqs[1:,]

freqschroma=np.asarray(np.log2(freqs)) - np.asarray([int(np.log2(f)) for f in freqs])

nchroma=len(chroma)
nfreqschroma=len(freqschroma)

CD=np.zeros((nfreqschroma, nchroma))

for i in range(nchroma):
CD[:,i] = np.abs(freqschroma - chroma[i])

FlipMatrix=np.flipud(CD)

min_index = []
min_value = []

for i in reversed(range(FlipMatrix.shape[0])):
index, value = min(enumerate(FlipMatrix[i]), key=operator.itemgetter(1))
min_index.append(index)
min_value.append(value)

CS = np.zeros((len(chroma),Pxx.shape[1]))

Magnitude= np.log(abs(Pxx[1:,]))

for i in range(CS.shape[0]):
a = [index for index,x in enumerate(min_index) if x == i]
AIndex = np.zeros((len(a),Pxx.shape[1]))
t=0;
for value in a:
    AIndex[t,:] = Magnitude[value,:]
    t=t+1
MeanMag=[]
for M in AIndex.T:
    MeanMag.append(np.mean(M))
CS[i,:] = MeanMag

CS= CS / CS.max()
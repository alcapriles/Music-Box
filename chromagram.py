import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sg
import math
import wave
import pylab
import operator

class Chromagram:
    
    def __init__(self, Nfft, A5, nbin, st, step, fr, df):
        self.Nfft=2048
        self.A5=880
        self.nbin=12
        self.st=2**(1/float(nbin))
        self.step=128
        self.fr=11025
        self.df=4
    
    def lilypondInput(self, colunas, notas):
        colunas = len(CS[1,:])
        notas = "\\relative c' { "
        for i in range(12):
            for j in range(colunas):
                if CS[i,j] > 0.95:
                    if i == 0:
                        notas += 'b '
                    elif i == 1:
                        notas += 'a-sharp '
                    elif i == 2:
                        notas += 'a '
                    elif i == 3:
                        notas += 'g-sharp '
                    elif i == 4:
                        notas += 'g '
                    elif i == 5:
                        notas += 'f-sharp '
                    elif i == 6:
                        notas += 'f '
                    elif i == 7:
                        notas += 'e '
                    elif i == 8:
                        notas += 'd-sharp '
                    elif i == 9:
                        notas += 'd '
                    elif i == 10:
                        notas += 'c-sharp '
                    elif i == 11:
                        notas.append += 'c '
        notas += '}'
        
        
    def chromagram(self):
        
        tunechroma1=[np.log2(A5*st**i) for i in range(nbin)] 
        tunechroma2=[int(np.log2(A5*st**i)) for i in range(nbin)]
        chroma=np.asarray(tunechroma1)-np.asarray(tunechroma2);
        
        spf = wave.open('background.wav','r')
        
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

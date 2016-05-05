import pyaudio
import wave
from GUI import GUI

class Record:
    
    def __init__(self, CHUNK, FORMAT, CHANNELS, RATE):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100

    #pedir ao usuário para dar um nome para o arquivo de áudio na interface
    WAVE_OUTPUT_FILENAME = "output.wav"
    # obs.:depois que a partitura for gerada, o arquivo de áudio deve ser apagado
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK)
    
    #colocar na interface gráfica: recording
    print("* recording")
    
    frames = []
    
    while (enquanto o evento de clique no botão de stop nao ocorrer)
        data = stream.read(CHUNK)
        frames.append(data)
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

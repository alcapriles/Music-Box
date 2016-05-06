import pyaudio
import wave

class Record:
    
    def __init__(self, CHUNK, FORMAT, CHANNELS, RATE):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.WAVE_OUTPUT_FILENAME = "output.wav"
        self.p = pyaudio.PyAudio()
        self.stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        self.frames = []
    
    def record(self):
        if is_recording:
            data = stream.read(CHUNK)
            frames.append(data)
            
            stream.stop_stream()
            stream.close()
            p.terminate()
        
    def encerrar(self): 
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

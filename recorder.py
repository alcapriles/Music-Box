import pyaudio
import wave

class Record():
    def __init__(self):

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
#o botao de gravar começa e termina, a linha seguinte irá sumir
RECORD_SECONDS = 5
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

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()


#while (enquanto o evento de clique no botão de stop nao ocorrer)
#    data = stream.read(CHUNK)
#    frames.append(data)

#stream.stop_stream()
#stream.close()
#p.terminate()


wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

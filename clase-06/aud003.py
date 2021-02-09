import pyaudio
import wave
import sys
from datetime import datetime

def to_integer(dt_time):
    return 10000000000*dt_time.year + 100000000*dt_time.month + 1000000*dt_time.day + 10000*dt_time.hour+100*dt_time.minute +dt_time.second

def aud003():
    now = datetime.now()
    wavfile = './data/audio-' + str(to_integer(now)) +'.wav'
    
    # Definicion de parametros
    FORMAT        = pyaudio.paInt16
    CHANNELS      = 1
    RATE          = 44100     # frecuencia de muestreo
    CHUNK         = 1024      # tamano del buffer
    RECORD_SECONDS= 5         # tiempo de grabacion
    
    # inicializa PyAudio
    audio = pyaudio.PyAudio()
    # sys.exit(0)

    # inicio de la grabacion
    stream = audio.open(
        format=FORMAT, 
        channels=CHANNELS,
        rate=RATE, 
        input=True, 
        frames_per_buffer=CHUNK
    )
    
    print("recording audio...")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("recording finished...")

    # stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # saving file 
    waveFile = wave.open(wavfile, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

aud003()
import pyaudio
import wave


def loadData():
    wavfile = './data/bird.wav'
    return wave.open(wavfile, 'rb')

def aud001():
    
    CHUNK = 1024          # numeros de frames en el buffer
   
    # inicializa PyAudio ---------------------------
    p = pyaudio.PyAudio()
    
    # propiedades del pyaudio
    print('formato   :', pyaudio.paInt8 )
    print('formato   :', pyaudio.paInt16)
    print('formato   :', pyaudio.paInt24)
    print('formato   :', pyaudio.paInt32)
    print('bytes x muestra')
    print('tamano muestra:', pyaudio.get_sample_size(pyaudio.paInt8 ))
    print('tamano muestra:', pyaudio.get_sample_size(pyaudio.paInt16))
    print('tamano muestra:', pyaudio.get_sample_size(pyaudio.paInt24))
    print('tamano muestra:', pyaudio.get_sample_size(pyaudio.paInt32))
    # sys.exit(0)

    # archivo a leer
    wf = loadData()
    
    # propiedades archivo
    print('formato   :', wf.getsampwidth())
    print('canales   :', wf.getnchannels()) # canales x buffer
    print('frecuencia:', wf.getframerate()) # muestras x seg
    print('bits      :', p.get_format_from_width(wf.getsampwidth()))
    
    # abrir el stream
    stream = p.open(format  = p.get_format_from_width(wf.getsampwidth()),
                    channels= wf.getnchannels(),
                    rate    = wf.getframerate(),
                    output  = True)
   
    # leer data
    data = wf.readframes(CHUNK)
    print(len(data))
    
    # ejecutar stream
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
        print(len(data))

    
    # detener stream (4)
    stream.stop_stream()
    stream.close()

    # cerrar PyAudio (5)
    p.terminate()        

    return
    
aud001()
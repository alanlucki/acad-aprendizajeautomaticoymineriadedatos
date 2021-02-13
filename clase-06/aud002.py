import pyaudio
from   wave     import open as open_wave
import sys
import numpy    as     np
import matplotlib.pyplot as plt
import struct

wavfile = './data/cat_y.wav'

# instanciacion de la libreria
p  = pyaudio.PyAudio()

# abrir el archivo
wf = open_wave(wavfile,'rb')

# propiedades archivo

'''
print('formato   :', wf.getsampwidth())
print('canales   :', wf.getnchannels()) # canales x buffer
print('frecuencia:', wf.getframerate()) # muestras x seg
print('bits      :', p.get_format_from_width(wf.getsampwidth()))
print('nframes   :', wf.getnframes())
'''

CHUNK     = wf.getnframes()
CHANELS   = wf.getnchannels()
wavFrames = wf.readframes(CHUNK)
print('dataframe :', len(wavFrames))

# convert to string
S = np.fromstring(wavFrames, dtype=np.int16)

# convert to float
U = struct.unpack("%ih" % (CHUNK * CHANELS / 2), wavFrames)
F = [float(val) / pow(2, 15) for val in U]

#print(len(F))
#print(list(F))

print(U)
#print(F)
#print(F)
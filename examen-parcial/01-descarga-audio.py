import os
import librosa
import ffmpy

import wave
import contextlib

from shutil import rmtree
from pytube import YouTube

def carpetas():
    try:
        rmtree("wav")
    except:
        print("no existe")
    
    try:
        rmtree("mp4")
    except:
        print("no existe")

    try:
        os.mkdir('wav')
    except:
        print("ya existe")

def descarga(x,y):
    print('Inicio la descarga de video de ', y)
    YouTube(x).streams.filter(only_audio=True).first().download('./mp4//audio/',y)
    print('Finalizo la descarga de video de ', y)
  
def convertir(x):
    
    origen = './mp4/audio/' + x + '.mp4'
    destino = './wav/' + x
    os.system('ffmpeg  -ss 00:00:00 -t 00:00:10 -i {} -acodec pcm_s16le -ar 44000 {}.wav'.format(origen,destino ) ) 

def segmentar(x,y):
    
    fname = './' + y + '.wav'
    duration = 0
    
    
    #for i in range(0, x):
        #origen = './wav/' + x + '.wav'
        #destino = './wav/' + x + '/' + x + "_" + i
        #tiempo_inici = i * duracion_segmento
        #tiempo_final = ( i + 1 ) * duracion_segmento
        #os.system('ffmpeg  -ss 00:00:' + tiempo_inici +' -t 00:00:' + tiempo_final +' -i {} -acodec pcm_s16le -ar 44000 {}.wav'.format(origen,destino ) ) 

    print (fname)
    
def procesar():


    print ('===============')
    print ('Descargar audio')
    print ('===============')
    print ('Inicio')
    print ('======')

    carpetas()

    links = [

        'https://www.youtube.com/watch?v=I087lKr0Z34&t=10s' , 
        'https://www.youtube.com/watch?v=hAqB1WxkZR0&t=10s' ,
        'https://www.youtube.com/watch?v=oNWGGTuAfTo&t=10s' ,
        'https://www.youtube.com/watch?v=iNVrelV5YK0&t=10s' ,
        'https://www.youtube.com/watch?v=QftIT_GeM74&t=10s' ,
        'https://www.youtube.com/watch?v=62fhUNdSOR4&t=10s' ,
        'https://www.youtube.com/watch?v=_HRJ-5sxg7s&t=10s' ,
        'https://www.youtube.com/watch?v=ZmlwAXHVuFU&t=10s',
        'https://www.youtube.com/watch?v=dcEMFdGaPAk&t=10s',
        'https://www.youtube.com/watch?v=RfG59eqe_Zk&t=10s'
    ]

    nombres = [
        
        '01-beto-ortiz' ,
        '02-rosa-palac',
        '03-cesa-hildr',
        '04-ceci-valen',
        '05-gonz-nunez',
        '06-dani-pered',
        '07-marc-deneg',
        '08-phil-butte',        
        '09-luis-trisa',
        '10-eric-osore'

    ]
    
    
    #for x in range(0, len(links)):
    for x in range(0, 1):
        descarga(links[x] ,nombres[x] )
        convertir(nombres[x])
        
        #print("Fecuencia = " + fs)
        #print("Periodo = " + (1.0/fs))
        segmentar(10,'wav/' + nombres[x])
        
        #data, fs = librosa.load('wav/' + nombres[x] +'.wav')
        
    try:
        rmtree("mp4")
    except:
        print("no existe")

    
    #print data 
    #print fs 

procesar()

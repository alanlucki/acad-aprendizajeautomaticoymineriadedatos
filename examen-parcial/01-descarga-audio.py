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
    
    duration = 0
    origen = 'wav/' + y +'.wav'
    
    with contextlib.closing(wave.open(origen,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        
    try:
        os.mkdir('wav/' + y)
    except:
        print("ya existe")

    for i in range(0, x):
        
        destino = 'wav/' + y + '/' +y +'_'+str(i + 1) 
        tiempo_inici = i * (duration/x)
        tiempo_final = ( i + 1 ) * (duration/x)
        print( "=" )
        print( i )
        print( "=" )

        str_inci = ''
        str_fina = ''
        if int(tiempo_inici) <= 10:
            str_inci = '0' + str(int(tiempo_inici))
        else:
            str_inci = str(int(tiempo_inici))

        if int(tiempo_final) < 10:
            str_fina = '0' + str(int(tiempo_final))
        else:
            str_fina = str(int(tiempo_final))
        
        print( 'ffmpeg  -ss 00:00:' + str_inci +' -t 00:00:' + str_fina +' -i {} -acodec pcm_s16le -ar 44000 {}.wav' )
        #os.system('ffmpeg  -ss 00:00:' + str_inci +' -t 00:00:' + str_fina +' -i {} -acodec pcm_s16le -ar 44000 {}.wav'.format(origen,destino ) ) 
        

    
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
        segmentar(10,nombres[x])
        
        #data, fs = librosa.load('wav/' + nombres[x] +'.wav')
        
    try:
        rmtree("mp4")
    except:
        print("no existe")

    
    #print data 
    #print fs 

procesar()

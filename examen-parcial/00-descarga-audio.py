import os
import librosa
import ffmpy
import time
import subprocess
import numpy as np
import pandas as pd
import wave
import contextlib
import pyaudio
import xlsxwriter
import math  
    
from shutil import rmtree
from pytube import YouTube
    
carpeta_wav = 'wav/'
carpeta_datos = 'datos/'
carpeta_estadisticas = 'estadisticas/'
        

def carpetas02():
    try:
        rmtree("mp4")
    except:
        print("no existe")

    try:
        os.mkdir('datos')
    except:
        print("ya existe")

    try:
        os.mkdir('estadisticas')
    except:
        print("ya existe")

def carpetas():
    try:
        rmtree("wav")
    except:
        print("no existe")
    try:
        rmtree("datos")
    except:
        print("no existe")
    
    try:
        rmtree("estadisticas")
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
    origen = carpeta_wav + y +'.wav'
    
    with contextlib.closing(wave.open(origen,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        
    try:
        os.mkdir(carpeta_wav + y)
    except:
        print("ya existe")

    for i in range(0, x):
        
        destino = carpeta_wav + y + '/' +y +'_'+str(i + 1)
        tiempo_inici = i * (duration/x)
        str_inci = ''
        if int(tiempo_inici) <= 10:
            str_inci = '0' + str(int(tiempo_inici))
        else:
            str_inci = str(int(tiempo_inici))

        str_duracion = ""
        if int((duration/x)) > 9:
            str_duracion = str(int((duration/x)))
        else:
            str_duracion = '0' + str(int((duration/x)))    

        os.system(str('ffmpeg -ss 00:00:' + str_inci +' -t 00:00:' + str_duracion + ' -i {} -acodec pcm_s16le -ar 44000 {}.wav').format(origen,destino ) )

def iterateDirectory(directory):
    ejemplo_dir = directory
    contenido = os.listdir(ejemplo_dir)    
    return contenido

def dataInicial():
    links = [

        'https://www.youtube.com/watch?v=I087lKr0Z34&t=10s' , 
        '''
        'https://www.youtube.com/watch?v=hAqB1WxkZR0&t=10s' ,
        'https://www.youtube.com/watch?v=oNWGGTuAfTo&t=10s' ,
        'https://www.youtube.com/watch?v=iNVrelV5YK0&t=10s' ,
        'https://www.youtube.com/watch?v=QftIT_GeM74&t=10s' ,
        'https://www.youtube.com/watch?v=62fhUNdSOR4&t=10s' ,
        'https://www.youtube.com/watch?v=_HRJ-5sxg7s&t=10s' ,
        'https://www.youtube.com/watch?v=ZmlwAXHVuFU&t=10s',
        'https://www.youtube.com/watch?v=dcEMFdGaPAk&t=10s',
        'https://www.youtube.com/watch?v=RfG59eqe_Zk&t=10s'
        '''
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
    
    atributos = [
        'atributo-01',
        'atributo-02',
        'atributo-03',
        'atributo-04',
        'atributo-05',
        'atributo-06'
    ]

    return links , nombres , atributos

def obtenerEstadisticas(df):

    estadisticos = {}
    estadisticos['sqrt(mean(sum))'] = math.sqrt(((df * df ).sum()).mean())
    estadisticos['Media'] = df.mean()     
    estadisticos['Media-absoluta'] = df.mean().mean()     
    estadisticos['Mediana'] = df.median()     
    estadisticos['Mediana-abosluta'] = df.median().median()     
    estadisticos['Desv-Est'] = df.std()     
    estadisticos['std/Media'] = df.std()/df.median()     
    estadisticos['Kurtosis'] = df.kurtosis()    
    estadisticos['Skewness'] = df.skew()   
                
    for j in range(0, 11):
        estadisticos['decil ' + str(j)] = df.quantile(0.10 *j )

    return estadisticos

def crearCsv(df,ruta):
    df.to_csv ( ruta, index = False, header=True)

def inicio():

    print ('===============')
    print ('Descargar audio')
    print ('===============')
    print ('Inicio')
    print ('======')

    
def procesar():
    
    
    carpetas()
    links , nombres , atributos = dataInicial()
    
    for x in range(0, len(links)):
        descarga(links[x] ,nombres[x] )
        convertir(nombres[x])
        segmentar(10,nombres[x])
    
    carpetas02()
    
    for i in range(0, len(links)):
        files = iterateDirectory(carpeta_wav+nombres[i]+'/') 
           
        matrizP = [{},{},{},{},{},{}]        
        
        for j in range(0, len(files)):
            y, sr = librosa.load(carpeta_wav+nombres[i]+'/'+ files[j] , duration = 1 )
            onset_env = librosa.onset.onset_strength(y, sr=sr)
            y_harm , y_perc = librosa.effects.hpss(y)
            cent = librosa.feature.spectral_centroid(y=y, sr=sr)
            contrast=librosa.feature.spectral_contrast(y=y_harm,sr=sr)
            zrate=librosa.feature.zero_crossing_rate(y_harm)
            
            matrizP[0][j] = y
            matrizP[1][j] = y_harm
            matrizP[2][j] = y_perc
            matrizP[3][j] = cent[0]
            matrizP[4][j] = contrast[0]
            matrizP[5][j] = zrate[0]
            
        print( '=========================================' )
        print( 'Periodista = ' + nombres[i] )
        print( '=========================================' )
        
        for p in range(0, len(matrizP)):

            df = pd.DataFrame(matrizP[p]) 
            estadisticas = obtenerEstadisticas(df)
            dfx = pd.DataFrame(estadisticas) 
            crearCsv(df,carpeta_datos +nombres[i] +'-' + atributos[p] + '.csv')
            crearCsv(dfx,carpeta_estadisticas +nombres[i] +'-' +  atributos[p]  + '.csv')
            print( dfx )
                                
procesar()

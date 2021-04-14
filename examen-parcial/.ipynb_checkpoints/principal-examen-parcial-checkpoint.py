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

def init():
    removeFolder('wav')
    removeFolder('datos')
    removeFolder('estadisticas')
    removeFolder('mp4')
    createFolder('wav')
    createFolder('datos')
    createFolder('estadisticas')
    createFolder('mp4')
def initialData():
    links = [
        'https://www.youtube.com/watch?v=I087lKr0Z34&t=10s' ,
        'https://www.youtube.com/watch?v=hAqB1WxkZR0&t=10s' ,
        'https://www.youtube.com/watch?v=oNWGGTuAfTo&t=10s' ,
        'https://www.youtube.com/watch?v=iNVrelV5YK0&t=10s' ,
        'https://www.youtube.com/watch?v=QftIT_GeM74&t=10s' ,
        'https://www.youtube.com/watch?v=62fhUNdSOR4&t=10s' ,
        'https://www.youtube.com/watch?v=_HRJ-5sxg7s&t=10s' ,
        'https://www.youtube.com/watch?v=ZmlwAXHVuFU&t=10s' ,
        'https://www.youtube.com/watch?v=dcEMFdGaPAk&t=10s' ,
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
    
    atributos = [
        'atributo-01-audio-time-series',
        'atributo-02-ritmo-armonico',
        'atributo-03-ritmo-percusivo',
        'atributo-04',
        'atributo-05',
        'atributo-06'
    ]

    return links , nombres , atributos
def removeFolder(x):
    try:
        rmtree(x)
    except:
        print("no existe")
def createFolder(x):
    try:
        os.mkdir(x)
    except:
        print("ya existe")
def segmentFile(x,y):
    duration = 0
    origen = carpeta_wav + y +'.wav'
    with contextlib.closing(wave.open(origen,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)

    createFolder(carpeta_wav + y)

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
def computeStad(df):
    estadisticos = {}
    estadisticos['sqrt(mean(sum))'] = math.sqrt(((df * df ).sum()).mean())
    estadisticos['Minimo'] = df.min()     
    estadisticos['Maximo'] = df.max()     
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
def matrixAtributes( files , nombre):
    m = [{},{},{},{},{},{}]        

    for j in range(0, len(files)):
        
        y, sr               = librosa.load(carpeta_wav+nombre+'/'+ files[j] , duration = 1 )        
        y_harm , y_perc     = librosa.effects.hpss(y)
        cent                = librosa.feature.spectral_centroid(y=y, sr=sr)
        contrast            = librosa.feature.spectral_contrast(y=y_harm,sr=sr)
        zrate               = librosa.feature.zero_crossing_rate(y_harm)
        
        '''
        Frecuencias central y anchura
        Frecuencias graves y agudas
        silencios
        '''

        m[0][j] = abs(y)                    # atributo 01 : audio time series
        m[1][j] = abs(y_harm )              # atributo 02 : ritmo armonico
        m[2][j] = abs(y_perc)               # atributo 03 : ritmo percusivo
        m[3][j] = cent[0]                   # atributo 04
        m[4][j] = contrast[0]               # atributo 05
        m[5][j] = zrate[0]                  # atributo 06
        
    return m                       


getFYoutube = lambda x,y:YouTube(x).streams.filter(only_audio=True).first().download('./mp4/audio/',y)
createCsv = lambda df,ruta : df.to_csv ( ruta, index = False, header=True)    
iterateDirectory = lambda directory: os.listdir(directory)    
convertFile = lambda x:os.system('ffmpeg  -ss 00:00:00 -t 00:00:10 -i {} -acodec pcm_s16le -ar 44000 {}.wav'.format('./mp4/audio/' + x + '.mp4','./wav/' + x ) ) 

def mainProcess():

    init()
    links , nombres , atributos = initialData()

    for i in range(0, len(links)):
        
        # Recorrer periodistas
        getFYoutube(links[i] ,nombres[i] )  # obtener videos desde youtube
        convertFile(nombres[i])             # convertir archivos mp4 -> wav
        segmentFile(10,nombres[i])          # dividir archivos
    
        files = iterateDirectory(carpeta_wav+nombres[i]+'/')            

        m = matrixAtributes(files , nombres[i])    
        
        print( '=========================================' )
        print( 'Periodista = ' + nombres[i] )
        print( '=========================================' )
        
        for j in range(0, len(m)):
            
            dfAtr = pd.DataFrame(m[j])      # dataframe de atributos obtenidos
            stadi = computeStad(dfAtr)      # dataframe de atributos obtenidos
            dfEst = pd.DataFrame(stadi)     # dataframe de estadisticas

            createCsv(dfAtr,carpeta_datos +nombres[i] +'-' + atributos[j] + '.csv')             # crea archivos csv atributos
            createCsv(dfEst,carpeta_estadisticas +nombres[i] +'-' +  atributos[j]  + '.csv')    # crea archivos csv estadisticas
            
            print( '=====================' )
            print( 'atributo = ' + atributos[j] )
            print( '=====================' )
            print( dfEst )

mainProcess()

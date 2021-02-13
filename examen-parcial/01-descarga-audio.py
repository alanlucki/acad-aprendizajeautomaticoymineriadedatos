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
        #tiempo_final = ( i + 1 ) * (duration/x)
        
        str_inci = ''
        #str_fina = ''
        
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

def exportarExcel(nombre,matriz):
    libro = xlsxwriter.Workbook(nombre + '.xlsx')
    hoja = libro.add_worksheet()

    presupuesto = (matriz)

    # Nos posicionamos en la primera columna de la primera fila
    row = 0
    col = 0
    
    # Iteramos los datos para ir pintando fila a fila
    for concepto, precio in (presupuesto):
        hoja.write(row, col,     concepto)
        hoja.write(row, col + 1, precio)
        row += 1
    
    #Pintamos la fila de totales
    hoja.write(row, 0, 'Total:')
    #hoja.write(row, 1, '=SUM(B1:B7)')
    
    #Cerramos el libro
    libro.close()

def getAtribute(x1,x2):
    matriz0 = {} 
    matriz1 = {} 
    matriz2 = {} 
    matriz3 = {} 
    matriz4 = {}

    for j in range(0, len(x1)):
        y, fs = librosa.load('wav/'+x2+'/'+ x1[j] )
        S_full, phase = librosa.magphase(librosa.stft(y))
        matriz0[j] = y
        matriz1[j] = S_full

    return [matriz0,matriz1]

def procesar():

   
    print ('===============')
    print ('Descargar audio')
    print ('===============')
    print ('Inicio')
    print ('======')

    carpetas()

    '''
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
    '''
    links = [

        'https://www.youtube.com/watch?v=I087lKr0Z34&t=10s' ,
        'https://www.youtube.com/watch?v=hAqB1WxkZR0&t=10s' ,
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
    
    
    for x in range(0, len(links)):
    #for x in range(0, 1):
        descarga(links[x] ,nombres[x] )
        convertir(nombres[x])
        segmentar(10,nombres[x])
    
    try:
        rmtree("mp4")
    except:
        print("no existe")

    for i in range(0, len(links)):
        arreglo = iterateDirectory('wav/'+nombres[i]+'/') 
        arregloAtributos = getAtribute(arreglo ,nombres[i]  )

        print( '=========================================' )
        print( 'Periodista = ' + nombres[i] )
        print( '=========================================' )
                
        for m in range(0, len(arregloAtributos)):
            
            df = pd.DataFrame(arregloAtributos[m]) 
            df.to_csv ( nombres[i] + str(m) +'.csv', index = False, header=True)

            arreglox ={}
            
            arreglox['xxxxxxxx'] = math.sqrt(((df * df ).sum()).mean())
            arreglox['Media'] = df.mean()     
            #arreglox['j+2'] = df.mean()     
            arreglox['Mediana'] = df.median()     
            #arreglox['j+4'] = df.median()     
            arreglox['Desv-Est'] = df.std()     
            arreglox['std/median'] = df.std()/df.median()     
            arreglox['Kurtosis'] = df.kurtosis()    
            arreglox['Skewness'] = df.skew()   
            
            for j in range(0, len(arreglo)+1):
                arreglox['decil ' + str(j)] = df.quantile(0.10 *j )

            dfx = pd.DataFrame(arreglox) 
            print( dfx )


procesar()

import os
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
    import ffmpy

    origen = './mp4/audio/' + x + '.mp4'
    destino = './wav/' + x

    os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}.wav'.format(origen,destino ) ) 

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
        '02-rosamaria-palacios',
        '03-cesar-hildrebrant',
        '04-cecilia-valenzuela',
        '05-gonzalo-nunez',
        '06-daniel-peredo',
        '07-marco-aurelio-denegri',
        '08-phillip-butter',        
        '09-luis-trisano',
        '10-erick-osores'

    ]
    
 
    for x in range(0, len(links)):
    #for x in range(0, 1):
        descarga(links[x] ,nombres[x] )
        convertir(nombres[x])

    try:
        rmtree("mp4")
    except:
        print("no existe")

procesar()

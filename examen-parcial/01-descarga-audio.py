'''
from pytube import YouTube
link = 'https://www.youtube.com/watch?v=U7JizpfSc1U'
youtube = YouTube(link)
stream = youtube.streams.filter(only_audio=True).all()
s.download('descarga')
'''
from pytube import YouTube
    

def descarga(link):
    yt = YouTube(link)
    
    #stream = yt.streams.filter(only_audio=True).all()
    #stream.download()
    

def procesar():
    
    print ('===============')
    print ('Descargar audio')
    print ('===============')
    print ('Inicio')
    print ('======')

    links = [
    
        'https://www.youtube.com/watch?v=KcMBekiA8Sc'
    
    ]

    for x in links:
        descarga(x)

    print ('===')
    print ('Fin')
    print ('===')


procesar()

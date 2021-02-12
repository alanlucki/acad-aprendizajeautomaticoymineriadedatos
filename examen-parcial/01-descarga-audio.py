'''
from pytube import YouTube
link = 'https://www.youtube.com/watch?v=U7JizpfSc1U'
youtube = YouTube(link)
stream = youtube.streams.filter(only_audio=True).all()
s.download('descarga')
'''

def descarga():
    youtube = YouTube(link)
    stream = youtube.streams.filter(only_audio=True).all()
    #stream.download('descarga')
    

def procesar():
    
    print ('===============')
    print ('Descargar audio')
    print ('===============')
    print ('Inicio')
    print ('======')

    from pytube import YouTube
    links = [
    
        'https://www.youtube.com/watch?v=KcMBekiA8Sc'
    
    ]

    print ('===')
    print ('Fin')
    print ('===')


procesar()

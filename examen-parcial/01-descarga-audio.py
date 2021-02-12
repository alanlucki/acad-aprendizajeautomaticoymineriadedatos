'''
from pytube import YouTube
link = 'https://www.youtube.com/watch?v=U7JizpfSc1U'
youtube = YouTube(link)
stream = youtube.streams.filter(only_audio=True).all()
s.download('descarga')
'''
print ('===============')
print ('Descargar audio')
print ('===============')
print ('Inicio')
print ('======')

from pytube import YouTube
links = [
    
    'https://www.youtube.com/watch?v=KcMBekiA8Sc'
    
]

youtube = YouTube(link)
stream = youtube.streams.filter(only_audio=True).all()
#stream.download('descarga')


print ('===')
print ('Fin')
print ('===')

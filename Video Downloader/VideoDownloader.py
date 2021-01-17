# pip install pytube
import pytube

url =  'https://www.youtube.com/watch?v=9bZkp7q19f0&ab_channel=officialpsy'
youtube = pytube.YouTube(url)

# Download na resolução mais alta disponivel
video = youtube.streams.get_highest_resolution()

# Local que o video vai ser salvo
video.download('')

print('Download finalizado')

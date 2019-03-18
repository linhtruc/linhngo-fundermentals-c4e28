#1

from urllib.request import urlopen
from bs4 import BeautifulSoup
# import pyexcel
from collections import OrderedDict

url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)

content = conn.read().decode('UTF-8')

soup = BeautifulSoup(content, "html.parser")

ul = soup.find("ul", "section-content")

li_list = ul.find_all("li")

list_song = []
for li in li_list:
    h4 = li.h4
    h3 = li.h3
    a4 = h4.a
    a3 = h3.a
    song_name = a3.string
    artist = a4.string
    
    dic = OrderedDict({
        "Song's name": song_name,
        "Artist": artist
    })
    list_song.append(dic)

print (list_song)
# pyexcel.save_as(records=list_song, dest_file_name="itune_song.xls")

#2
from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(song_name, artist)

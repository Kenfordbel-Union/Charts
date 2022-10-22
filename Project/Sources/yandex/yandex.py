import os

import yandex_music
from yandex_music import Client
import pymongo
CHART_ID = 'ukraine'
TOKEN = os.environ.get('AQAAAABiu4_vAAgJ512cuW5RwU8HsyJ7W0gZEls')

mongo = pymongo.MongoClient()
mydb = mongo["charts"]
mycollection = mydb["yandex"]
#ДОБАВИТЬ ИНТЕРВАЛ, КАЖДЫЕ СУТКИ
def collect_yandex_charts():
    num = 0
    client = Client(TOKEN).init()
    chart = client.chart(CHART_ID).chart
    for track_short in chart.tracks:
        track, chart = track_short.track, track_short.chart
        artists = ''
        if track.artists:
            artists = ' - ' + ', '.join(artist.name for artist in track.artists)
        track_text = f'{track.title}{artists}'
        artist_and_song_for_db = {f"song-{num}": track_text}
        num = num + 1
        mycollection.insert_one(artist_and_song_for_db)
        if num > 49:
            break
collect_yandex_charts()

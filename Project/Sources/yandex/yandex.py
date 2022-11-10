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
    client = Client(TOKEN).init()
    chart = client.chart(CHART_ID).chart
    num = 0
    text = [f'🏆 {chart.title}', chart.description, '', 'Треки:']
    # list_of_songs = {}
    for track_short in chart.tracks:
    #      track = track_short['track']
    #      track_name = track["title"]
    #      artist = track['artists']
    #      remove_list = artist[0]
    #      artist_name = remove_list['name']
    #      list_of_songs[artist_name] = track_name
    #      response = f"{artist_name} - {track_name}"
    # print(list_of_songs)
        track, chart = track_short.track, track_short.chart
        artists = ''
        if track.artists:
            artists = ' - ' + ', '.join(artist.name for artist in track.artists)
        track_text = f'{track.title}{artists}'
        if chart.progress == 'down':
            track_text = '🔻 ' + track_text
        elif chart.progress == 'up':
            track_text = '🔺 ' + track_text
        elif chart.progress == 'new':
            track_text = '🆕 ' + track_text
        elif chart.position == 1:
            track_text = '👑 ' + track_text
        track_text = {f'song-{num}': f'{chart.position} {track_text}'}
        mycollection.insert_one(track_text)

        print(track_short)
        break

collect_yandex_charts()



# def collect_yandex_charts():
#     num = 0
#     client = Client(TOKEN).init()
#     chart = client.chart(CHART_ID).chart
#     for track_short in chart.tracks:
#         track, chart = track_short.track, track_short.chart
#         artists = ''
#         if track.artists:
#             artists = ' - ' + ', '.join(artist.name for artist in track.artists)
#         track_text = f'{track.title}{artists}'
#         artist_and_song_for_db = {f"song-{num}": track_text}
#         num = num + 1
#         mycollection.insert_one(artist_and_song_for_db)
#         if num > 49:
#             break
# collect_yandex_charts()

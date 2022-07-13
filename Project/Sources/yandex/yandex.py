import os
from yandex_music import Client
import json
CHART_ID = 'belarus'
TOKEN = os.environ.get('AQAAAABiu4_vAAgJ512cuW5RwU8HsyJ7W0gZEls')

def collect_yandex_charts():
    client = Client(TOKEN).init()
    chart = client.chart(CHART_ID).chart
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
        track_text = f'{chart.position} {track_text}'
        text.append(track_text)
    a = '\n'.join(text)
    print(a)

collect_yandex_charts()
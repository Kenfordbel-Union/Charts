import os
from yandex_music import Client
import json
CHART_ID = 'belarus'
TOKEN = os.environ.get('AQAAAABiu4_vAAgJ512cuW5RwU8HsyJ7W0gZEls')

def collect_yandex_charts():
    client = Client(TOKEN).init()
    chart = client.chart(CHART_ID).chart
    list_of_songs = {}
    for track_short in chart.tracks:
          track = track_short['track']
          track_name = track["title"]
          artist = track['artists']
          remove_list = artist[0]
          artist_name = remove_list['name']
          list_of_songs[artist_name] = track_name
          response = f"{artist_name} - {track_name}"
    print(list_of_songs)

    with open("yandex_data.json", "w") as outfile:
        a = json.dump(list_of_songs, outfile)

collect_yandex_charts()
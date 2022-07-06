import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import client
import pandas as pd

cid = 'dbf0dc8d604c4c609128508a05aaf09e'
secret = 'ba6756bbc94249f58737f36628451743'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
creator = "spotify"
playlist_id = "37i9dQZEVXbMDoHDwVN2tF"
data = sp.playlist_tracks(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))
data = data['items']
# position = data[0]
for i in data:
    track_info = i['track']
    artist = track_info['artists']
    artist_name = artist[0]['name']
    track = track_info['name']
    print(f"{artist_name} - {track}")
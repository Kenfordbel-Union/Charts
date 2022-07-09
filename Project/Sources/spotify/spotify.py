import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

cid = 'dbf0dc8d604c4c609128508a05aaf09e'
secret = 'ba6756bbc94249f58737f36628451743'

def collect_spotify_charts():
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlist_id = "37i9dQZEVXbLRLeF2cVSaP"
    data = sp.playlist_tracks(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))
    data = data['items']
    num = 0
    list_of_songs = {}
    for each in data:
        track_info = each['track']
        artist = track_info['artists']
        artist_name = artist[0]['name']
        track = track_info['name']
        list_of_songs[artist_name] = track
        num = num+1
    with open("spotify_data.json", "w") as outfile:
        a = json.dump(list_of_songs, outfile)
collect_spotify_charts()
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pymongo
cid = 'dbf0dc8d604c4c609128508a05aaf09e'
secret = 'ba6756bbc94249f58737f36628451743'

mongo = pymongo.MongoClient()
mydb = mongo["charts"]
mycollection = mydb["spotify"]
#ДОБАВИТЬ ИНТЕРВАЛ, КАЖДЫЕ СУТКИ
def collect_spotify_charts():
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlist_id = "37i9dQZEVXbLRLeF2cVSaP"
    data = sp.playlist_tracks(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))
    data = data['items']
    num = 0
    num2 = 0
    for each in data:
        track_info = each['track']
        artist = track_info['artists']
        artist_name = artist[0]['name']
        artist_name_for_db = {f"artist-{num}":artist_name}
        num = num+1
        db_insert_artist = mycollection.insert_one(artist_name_for_db)
        track = track_info['name']
        track_name_for_db = {f"track-{num2}":track}
        num2 = num2+1
        db_insert_track = mycollection.insert_one(track_name_for_db)
collect_spotify_charts()

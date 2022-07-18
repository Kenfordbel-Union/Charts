import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pymongo
cid = 'dbf0dc8d604c4c609128508a05aaf09e'
secret = 'ba6756bbc94249f58737f36628451743'

mongo = pymongo.MongoClient()

charts_db = mongo["charts"]
songs_col = charts_db["spotify"]


#ДОБАВИТЬ ИНТЕРВАЛ, КАЖДЫЕ СУТКИ
def collect_spotify_charts():
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlist_id = "37i9dQZEVXbNG2KDcFcKOF"
    playlist_id_belarus = "37i9dQZEVXbLRLeF2cVSaP"
    data = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))
    data = data['items']
    num = 0
    num2 = 0
    for song in data:
        track_info = song['track']
        img = track_info['album']
        images = img['images']
        small_logo = images[1]
        finally_logo = small_logo['url']
        artist = track_info['artists']
        artist_name = artist[0]['name']
        track = track_info['name']
        song_for_db = {f"song-{num}":f"{track} - {artist_name}"}
        db_insert_songs = songs_col.insert_one(song_for_db)
        urls = track_info['preview_url']
        if urls == None:
            result = songs_col.update_one(
                {f"song-{num}": f"{track} - {artist_name}"},
                {
                    "$set": {
                        f"logo-{num}": f"{finally_logo}",
                        f"sing-{num}": f"/filter",
                    },
                    "$currentDate": {"lastModified": True}
                }
            )
            num = num+1
        else:
            result = songs_col.update_one(
                {f"song-{num}": f"{track} - {artist_name}"},
                {
                    "$set": {
                        f"logo-{num}": f"{finally_logo}",
                        f"sing-{num}": f"{urls}",
                    },
                    "$currentDate": {"lastModified": True}
                }
            )
            num = num + 1
collect_spotify_charts()


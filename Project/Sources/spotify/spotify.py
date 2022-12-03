import uuid
import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pymongo
cid = 'dbf0dc8d604c4c609128508a05aaf09e'
secret = 'ba6756bbc94249f58737f36628451743'

mongo = pymongo.MongoClient()

charts_db = mongo["charts"]
songs_col = charts_db["spotify"]
songs_col2 = charts_db["spotify2"]

worldwide = "37i9dQZEVXbNG2KDcFcKOF"
ukraine = "37i9dQZEVXbNcoJZ65xktI"
usa = "37i9dQZF1DX0kbJZpiYdZl"
spain = "37i9dQZEVXbMfVLvbaC3bj"
france = "1B8UQSO6ecpMHFCoR5VNj7"
belarus = "37i9dQZEVXbIYfjSLbWr4V"

def pos_checker(song_id, num, id):
    a = songs_col2.find_one({"_song_id": song_id})
    if a != None:
        a = list(a)
        sing_num = sorted(a)
        sing_num = sing_num[5]
        sing_num = sing_num.split('-', 1)
        diff_num = int(sing_num[1])
        if diff_num < num:
            return "🔻 "
        elif diff_num > num:
            return "🔺 "
        else:
            return ""
    else:
        return "🆕 "

def collect_spotify_charts(playlist_id, id):
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    data = sp.playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))
    data = data['items']
    num = 0
    for song in data:
        track_info = song['track']
        img = track_info['album']
        images = img['images']
        small_logo = images[1]
        finally_logo = small_logo['url']
        artist = track_info['artists']
        artist_name = artist[0]['name']
        track = track_info['name']
        track_with_artist = f"{track} - {artist_name}"
        song_for_db = {f"{id}song-{num}":f"{pos_checker(track_with_artist, num, id)}{track} - {artist_name}"}
        db_insert_songs = songs_col.insert_one(song_for_db)
        urls = track_info['preview_url']
        if urls == None:
            result = songs_col.update_one(
                {f"{id}song-{num}": f"{pos_checker(track_with_artist, num, id)}{track} - {artist_name}"},
                {
                    "$set": {
                        f"{id}logo-{num}": f"{finally_logo}",
                        f"{id}sing-{num}": f"/filter",
                        f"{id}url-{num}": str(uuid.uuid4()),
                        "likes": 0,
                        "xcomments": [],
                        "_song_id": f"{track} - {artist_name}"
                    },
                    "$currentDate": {"lastModified": True}
                }
            )
            num = num+1
        else:
            result = songs_col.update_one(
                {f"{id}song-{num}": f"{pos_checker(track_with_artist, num, id)}{track} - {artist_name}"},
                {
                    "$set": {
                        f"{id}logo-{num}": f"{finally_logo}",
                        f"{id}sing-{num}": f"{urls}",
                        f"{id}url-{num}": str(uuid.uuid4()),
                        "likes": 0,
                        "xcomments": [],
                        "_song_id": f"{track} - {artist_name}"
                    },
                    "$currentDate": {"lastModified": True}
                }
            )
            num = num + 1

songs_col2.drop({})
for i in songs_col.find():
    songs_col2.insert_one(i)
songs_col.drop({})

collect_spotify_charts(worldwide, "")
collect_spotify_charts(ukraine, "ua")
collect_spotify_charts(usa, "usa")
collect_spotify_charts(spain, "spa")
collect_spotify_charts(france, "sfra")
collect_spotify_charts(belarus, "sbel")


import pymongo
mongo = pymongo.MongoClient()
songs_db = mongo["charts"]

spotify = songs_db["spotify"]

yandex = songs_db["yandex"]

youtube = songs_db["youtube"]

deezer = songs_db["deezer"]


def erase_all_collections(song_spotify, song_yandex, song_deezer, song_yt):
    song_spotify.drop({})
    song_yandex.drop({})
    song_yt.drop({})
    song_deezer.drop({})


erase_all_collections(spotify, yandex, deezer, youtube)

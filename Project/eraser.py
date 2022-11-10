import pymongo
mongo = pymongo.MongoClient()
songs_db = mongo["charts"]

yandex = songs_db["yandex"]

youtube = songs_db["youtube"]

deezer = songs_db["deezer"]

general = songs_db["general"]


def erase_all_collections(song_yandex, song_deezer, song_yt, song_general):
    song_yandex.drop({})
    song_yt.drop({})
    song_deezer.drop({})
    song_general.drop({})


erase_all_collections(yandex, deezer, youtube, general)

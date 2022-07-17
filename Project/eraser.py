import pymongo
mongo = pymongo.MongoClient()
songs_db = mongo["charts"]

spotify = songs_db["spotify"]

yandex = songs_db["yandex"]

youtube = songs_db["youtube"]


def erase_all_collections(song_spotify, song_yandex, song_yt):
    song_spotify.drop({})
    song_yandex.drop({})
    song_yt.drop({})


erase_all_collections(spotify, yandex, youtube)
##ЗАСУНУТЬ ПЕРЕД ВОРКЕРАМИ ВСЁ В ОДНУ ФУНКЦИЮ

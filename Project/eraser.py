import pymongo
mongo = pymongo.MongoClient()
songs_db = mongo["charts"]

spotify = songs_db["spotify"]

yandex = songs_db["yandex"]


def erase_all_collections(song_spotify, song_yandex,):
    song_spotify.drop({})
    song_yandex.drop({})


erase_all_collections(spotify, yandex)
##ЗАСУНУТЬ ПЕРЕД ВОРКЕРАМИ ВСЁ В ОДНУ ФУНКЦИЮ

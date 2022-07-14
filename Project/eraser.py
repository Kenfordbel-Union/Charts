import pymongo
mongo = pymongo.MongoClient()
mydb = mongo["charts"]
spotify = mydb["spotify"]
yandex = mydb["yandex"]
def erase_all_collections(col1, col2):
    col1.drop({})
    col2.drop({})


erase_all_collections(spotify,yandex)
##ЗАСУНУТЬ ПЕРЕД ВОРКЕРАМИ ВСЁ В ОДНУ ФУНКЦИЮ

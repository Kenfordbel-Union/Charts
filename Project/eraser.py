import pymongo
import time
import schedule
mongo = pymongo.MongoClient()
mydb = mongo["charts"]
spotify = mydb["spotify"]
yandex = mydb["yandex"]
def erase_all_collections(col1, col2):
    col1.drop({})
    col2.drop({})

##ЗАСУНУТЬ ПЕРЕД ВОРКЕРАМИ ВСЁ В ОДНУ ФУНКЦИЮ

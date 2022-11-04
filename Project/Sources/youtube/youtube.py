from ytmusicapi import YTMusic
import pymongo
import uuid

mongo = pymongo.MongoClient()

charts_db = mongo["charts"]
youtube = charts_db["youtube"]
default = "https://music.youtube.com/watch?v="


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
    "X-Goog-AuthUser": "0",
    "x-origin": "https://music.youtube.com",
    "Cookie" : "VISITOR_INFO1_LIVE=3fKzDp-ZVBE; CONSENT=YES+BY.ru+201910; LOGIN_INFO=AFmmF2swRQIgRc7JW3KzLT46-NULPlkoo7KBVVNb9OrNd2yGlBX_PAMCIQDlF37bO3apI3jdI8J0VMI1FTbHmbmWzHCp_DtuFQ4Y9Q:QUQ3MjNmeGhFRTF4MW5HMWlPeF84SG9mYnNIdENWMktyQUR1cjJDYzY4SWR3czVETGt0UnhndU1OVER4c2NFZm00NFpXUUYyTVlpVlExY1FneGxUWFZEWEZOZEF2eUc5Wi0wODcwMGZqYkZBZ01UcEhqT2dSeGxtMVhiSGhZQU8xWFV5MHZRNUFRSVJycW9wNFM4Q1g5UUEtREFtdF9meFpzR0MyTk40ZDhXcEZEZWFtclU4R1ZKNkRlYWdTd0M4aHZmU2dVQVk5TXJJ; PREF=cvdm=grid&gl=BY&tz=Europe.Minsk&al=ru&f5=30030&f4=4000000; HSID=AVCBEdq8Fkpcn7lbq; SSID=ATzQExEjdTnfz9Bgu; APISID=I1-LtYjaFGRf0TWs/AsjHlouaQOSi8oDPe; SAPISID=pIPVGm8h53Q71yVO/AVPxvEkjI93wCjama; __Secure-1PAPISID=pIPVGm8h53Q71yVO/AVPxvEkjI93wCjama; __Secure-3PAPISID=pIPVGm8h53Q71yVO/AVPxvEkjI93wCjama; _gcl_au=1.1.1937999735.1657831280; SID=MQgx35KYAIwpRQfG-54qX0hAdisXipVCOT7-Ylyw4xOGWoZ5naxXcrc-rVvosdnHNpCNLA.; __Secure-1PSID=MQgx35KYAIwpRQfG-54qX0hAdisXipVCOT7-Ylyw4xOGWoZ5y8GmvcRs4utpFPOfT4Z6Zg.; __Secure-3PSID=MQgx35KYAIwpRQfG-54qX0hAdisXipVCOT7-Ylyw4xOGWoZ5h6zo9SC8SuXZbEwvA9dqGQ.; YSC=XIHH4-wE6dM; SIDCC=AJi4QfEon_XI8SZ8xwsPNHtGNjJXNwClkLyLIFtk3lBwTndBxThQBu-PYqK1ob7TY2Q8zWmklzUq; __Secure-1PSIDCC=AJi4QfH_hTNxzQtz_pycYuqKTaxxPo55zdzVLyNjtdERkPGYplcvT5_4gbT4eUKrwVtLJiPU8w; __Secure-3PSIDCC=AJi4QfFapfD8aNCi1JNVEv0HJXOZjdAse7zx6UMf3VbovjGlxynoA26h3VPNMyklsh3KqG8k0vVC"
}

ytmusic = headers
YTMusic = YTMusic()

charts = YTMusic.get_charts(country='ZZ') #это и так готовые функции, их не надо оборачивать
chartsua = YTMusic.get_charts(country='UA')
chartsusa = YTMusic.get_charts(country='US')
chartsspa = YTMusic.get_charts(country='ES')
chartsfra = YTMusic.get_charts(country='FR')


data = charts['videos']
dataua = chartsua['videos']
datausa = chartsusa['videos']
dataspa = chartsspa['videos']
datafra = chartsfra['videos']

pesni = data['items']
pesniua = dataua['items']
pesniusa = datausa['items']
pesnispa = dataspa['items']
pesnifra = datafra['items']

num = 0
numua = 0
numusa = 0
numspa = 0
numfra = 0
for track in pesni:
    title = track['title']
    video_id = track['videoId']
    artists = track['artists']
    image_path = track['thumbnails'][0]
    image = image_path['url']
    list = []
    for i in artists:
        artist_count = len(artists) - 1
        name = i['name']
        list.append(name)
    listless = ', '.join(list)
    song_for_db = {f"song-{num}":f"{title} - {listless}"}

    db_insert_songs = youtube.insert_one(song_for_db)

    result = youtube.update_one(
        {f"song-{num}": f"{title} - {listless}"},
        {
            "$set": {
                f"logo-{num}": f"{image}",
                f"sing-{num}": f"{default + video_id}",
                f"url-{num}": str(uuid.uuid4()),
                "likes": 0
            },
            "$currentDate": {"lastModified": True}
        }
    )
    num = num + 1

for track in pesniua:
    title = track['title']
    video_id = track['videoId']
    artists = track['artists']
    image_path = track['thumbnails'][0]
    image = image_path['url']
    list = []
    for i in artists:
        artist_count = len(artists) - 1
        name = i['name']
        list.append(name)
    listless = ', '.join(list)
    song_for_db = {f"uasong-{numua}":f"{title} - {listless}"}

    db_insert_songs = youtube.insert_one(song_for_db)

    result = youtube.update_one(
        {f"uasong-{numua}": f"{title} - {listless}"},
        {
            "$set": {
                f"ualogo-{numua}": f"{image}",
                f"uasing-{numua}": f"{default + video_id}",
                f"uaurl-{numua}": str(uuid.uuid4()),
                "likes": 0
            },
            "$currentDate": {"lastModified": True}
        }
    )
    numua = numua + 1

for track in pesniusa:
    title = track['title']
    video_id = track['videoId']
    artists = track['artists']
    image_path = track['thumbnails'][0]
    image = image_path['url']
    list = []
    for i in artists:
        artist_count = len(artists) - 1
        name = i['name']
        list.append(name)
    listless = ', '.join(list)
    song_for_db = {f"usasong-{numusa}":f"{title} - {listless}"}

    db_insert_songs = youtube.insert_one(song_for_db)

    result = youtube.update_one(
        {f"usasong-{numusa}": f"{title} - {listless}"},
        {
            "$set": {
                f"usalogo-{numusa}": f"{image}",
                f"usasing-{numusa}": f"{default + video_id}",
                f"usaurl-{numusa}": str(uuid.uuid4()),
                "likes": 0
            },
            "$currentDate": {"lastModified": True}
        }
    )
    numusa = numusa + 1

for track in pesnispa:
    title = track['title']
    video_id = track['videoId']
    artists = track['artists']
    image_path = track['thumbnails'][0]
    image = image_path['url']
    list = []
    for i in artists:
        artist_count = len(artists) - 1
        name = i['name']
        list.append(name)
    listless = ', '.join(list)
    song_for_db = {f"spasong-{numspa}":f"{title} - {listless}"}

    db_insert_songs = youtube.insert_one(song_for_db)

    result = youtube.update_one(
        {f"spasong-{numspa}": f"{title} - {listless}"},
        {
            "$set": {
                f"spalogo-{numspa}": f"{image}",
                f"spasing-{numspa}": f"{default + video_id}",
                f"spaurl-{numspa}": str(uuid.uuid4()),
                "likes": 0
            },
            "$currentDate": {"lastModified": True}
        }
    )
    numspa = numspa + 1

for track in pesnifra:
    title = track['title']
    video_id = track['videoId']
    artists = track['artists']
    image_path = track['thumbnails'][0]
    image = image_path['url']
    list = []
    for i in artists:
        artist_count = len(artists) - 1
        name = i['name']
        list.append(name)
    listless = ', '.join(list)
    song_for_db = {f"sfrasong-{numfra}":f"{title} - {listless}"}

    db_insert_songs = youtube.insert_one(song_for_db)

    result = youtube.update_one(
        {f"sfrasong-{numfra}": f"{title} - {listless}"},
        {
            "$set": {
                f"sfralogo-{numfra}": f"{image}",
                f"sfrasing-{numfra}": f"{default + video_id}",
                f"sfraurl-{numfra}": str(uuid.uuid4()),
                "likes": 0
            },
            "$currentDate": {"lastModified": True}
        }
    )
    numfra = numfra + 1



from ytmusicapi import YTMusic
import pymongo

mongo = pymongo.MongoClient()

charts_db = mongo["charts"]
songs_col = charts_db["youtube"]
default = "https://music.youtube.com/watch?v=NbB6qMA2lts&list="

ytmusic = YTMusic('headers_auth.json')
YTMusic = YTMusic()
charts = YTMusic.get_charts(country='UA') #это и так готовые функции, их не надо оборачивать

num = 0
data = charts['videos']
pesni = data['items']
counter = 0
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

    db_insert_songs = songs_col.insert_one(song_for_db)

    result = songs_col.update_one(
        {f"song-{num}": f"{title} - {listless}"},
        {
            "$set": {
                f"logo-{num}": f"{image}",
                f"link-{num}": f"{default + video_id}"
            },
            "$currentDate": {"lastModified": True}
        }
    )
    num = num + 1









    # title = items[0]['title']
    # is_artist = items[0]['artists']
    # try:
    #     artists = is_artist[0]["name"]
    #     artists2 = is_artist[1]["name"]
    #     print(artists, artists2)
    # except:
    #     print("lose")
    # break


    #
    # def check_artists():
    #     for every in is_artist:
    #         artist = every['name']
    #         print(artist)
    #         return artist
    # print(f"{artist} - {title}")
    #
    # break


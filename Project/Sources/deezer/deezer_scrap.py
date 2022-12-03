import deezer
import pymongo
import uuid

mongo = pymongo.MongoClient()

charts_db = mongo["charts"]
songs_col = charts_db["deezer"]
songs_col2 = charts_db["deezer2"]

global_charts = 3155776842
ua_charts = 1362526495
usa_charts = 1313621735
spain_charts = 1116190041
france_charts = 1109890291
belarus_chart = 1116189381

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

def scrap_deezer(chart_id, id):
    client = deezer.Client()
    data = client.get_playlist(chart_id).as_dict()

    data = data['tracks']
    num = 0
    for track in data:
        if num < 50:
            name = track['title']
            artist_name = track['artist']['name']
            sing_preview_link = track['preview']
            image = track['album']['cover_medium']
            song_link = track['link']
            track_with_artist = f"{name} - {artist_name}"
            song_for_db = {f"{id}song-{num}": f"{pos_checker(track_with_artist, num, id)}{name} - {artist_name}"}
            db_insert_songs = songs_col.insert_one(song_for_db)
            if song_link == None:
                result = songs_col.update_one(
                    {f"{id}song-{num}": f"{pos_checker(track_with_artist, num, id)}{name} - {artist_name}"},
                    {
                        "$set": {
                            f"{id}logo-{num}": f"{image}",
                            f"{id}sing-{num}": f"/filter",
                            f"{id}url-{num}": str(uuid.uuid4()),
                            "likes": 0,
                            "xcomments": [],
                            "_song_id": f"{name} - {artist_name}"
                        },
                        "$currentDate": {"lastModified": True}
                    }
                )
                num += 1
            else:
                result = songs_col.update_one(
                    {f"{id}song-{num}": f"{pos_checker(track_with_artist, num, id)}{name} - {artist_name}"},
                    {
                        "$set": {
                            f"{id}logo-{num}": f"{image}",
                            f"{id}sing-{num}": f"{sing_preview_link}",
                            f"{id}url-{num}": str(uuid.uuid4()),
                            "likes": 0,
                            "xcomments": [],
                            "_song_id": f"{name} - {artist_name}"
                        },
                        "$currentDate": {"lastModified": True}
                    }
                )

                num += 1

songs_col2.drop({})
for i in songs_col.find():
    songs_col2.insert_one(i)
songs_col.drop({})

scrap_deezer(global_charts, "")
scrap_deezer(ua_charts, "ua")
scrap_deezer(usa_charts, "usa")
scrap_deezer(spain_charts, "spa")
scrap_deezer(france_charts, "sfra")
scrap_deezer(belarus_chart, "sbel")

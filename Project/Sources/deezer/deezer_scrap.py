import deezer
import pymongo

mongo = pymongo.MongoClient()

charts_db = mongo["charts"]
songs_col = charts_db["deezer"]

global_charts = 3155776842
ua_charts = 1362526495
usa_charts = 1313621735
spain_charts = 1116190041
france_charts = 1109890291

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
            song_for_db = {f"{id}song-{num}": f"{name} - {artist_name}"}
            db_insert_songs = songs_col.insert_one(song_for_db)
            if song_link == None:
                result = songs_col.update_one(
                    {f"{id}song-{num}": f"{name} - {artist_name}"},
                    {
                        "$set": {
                            f"{id}logo-{num}": f"{image}",
                            f"{id}link-{num}": f"{song_link}",
                            f"{id}sing-{num}": f"/filter",
                        },
                        "$currentDate": {"lastModified": True}
                    }
                )
                num += 1
            else:
                result = songs_col.update_one(
                    {f"{id}song-{num}": f"{name} - {artist_name}"},
                    {
                        "$set": {
                            f"{id}logo-{num}": f"{image}",
                            f"{id}link-{num}": f"{song_link}",
                            f"{id}sing-{num}": f"{sing_preview_link}",
                        },
                        "$currentDate": {"lastModified": True}
                    }
                )

                num += 1


scrap_deezer(global_charts, "")
scrap_deezer(ua_charts, "ua")
scrap_deezer(usa_charts, "usa")
scrap_deezer(spain_charts, "spa")
scrap_deezer(france_charts, "fra")

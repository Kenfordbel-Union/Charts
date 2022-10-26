import deezer
import pymongo

mongo = pymongo.MongoClient()

charts_db = mongo["charts"]
songs_col = charts_db["deezer"]


def scrap_deezer():
    client = deezer.Client()

    global_charts = 3155776842
    data = client.get_playlist(global_charts).as_dict()

    data = data['tracks']
    num = 0
    for track in data:
        if num < 50:
            name = track['title']
            artist_name = track['artist']['name']
            sing_preview_link = track['preview']
            image = track['album']['cover_medium']
            song_link = track['link']
            song_for_db = {f"song-{num}": f"{name} - {artist_name}"}
            db_insert_songs = songs_col.insert_one(song_for_db)
            if song_link == None:
                result = songs_col.update_one(
                    {f"song-{num}": f"{name} - {artist_name}"},
                    {
                        "$set": {
                            f"logo-{num}": f"{image}",
                            f"link-{num}": f"{song_link}",
                            f"sing-{num}": f"/filter",
                        },
                        "$currentDate": {"lastModified": True}
                    }
                )
                num += 1
            else:
                result = songs_col.update_one(
                    {f"song-{num}": f"{name} - {artist_name}"},
                    {
                        "$set": {
                            f"logo-{num}": f"{image}",
                            f"link-{num}": f"{song_link}",
                            f"sing-{num}": f"{sing_preview_link}",
                        },
                        "$currentDate": {"lastModified": True}
                    }
                )

                num += 1


scrap_deezer()

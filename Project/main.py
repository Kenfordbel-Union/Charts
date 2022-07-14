from flask import Flask, render_template
import pymongo
mongo = pymongo.MongoClient()
mydb = mongo["charts"]
spotify = mydb["spotify"]
yandex = mydb["yandex"]
app = Flask(__name__)

@app.route('/')
def index():
    artist1 = spotify.find_one({"artist-0": {"$exists": "true"}})['artist-0']
    song1 = spotify.find_one({"track-0": {"$exists": "true"}})['track-0']
    artist2 = spotify.find_one({"artist-1": {"$exists": "true"}})['artist-1']
    song2 = spotify.find_one({"track-1": {"$exists": "true"}})['track-1']
    artist3 = spotify.find_one({"artist-2": {"$exists": "true"}})['artist-2']
    song3 = spotify.find_one({"track-2": {"$exists": "true"}})['track-2']
    artist4 = spotify.find_one({"artist-3": {"$exists": "true"}})['artist-3']
    song4 = spotify.find_one({"track-3": {"$exists": "true"}})['track-3']

    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']
    yandex2 = yandex.find_one({"song-1": {"$exists": "true"}})['song-1']
    yandex3 = yandex.find_one({"song-2": {"$exists": "true"}})['song-2']
    yandex4 = yandex.find_one({"song-3": {"$exists": "true"}})['song-3']
    yandex5 = yandex.find_one({"song-4": {"$exists": "true"}})['song-4']
    yandex6 = yandex.find_one({"song-5": {"$exists": "true"}})['song-5']
    yandex7 = yandex.find_one({"song-6": {"$exists": "true"}})['song-6']
    yandex8 = yandex.find_one({"song-7": {"$exists": "true"}})['song-7']
    yandex9 = yandex.find_one({"song-8": {"$exists": "true"}})['song-8']
    yandex10 = yandex.find_one({"song-9": {"$exists": "true"}})['song-9']

    yandex11 = yandex.find_one({"song-10": {"$exists": "true"}})['song-10']
    yandex12 = yandex.find_one({"song-11": {"$exists": "true"}})['song-11']
    yandex13 = yandex.find_one({"song-12": {"$exists": "true"}})['song-12']
    yandex14 = yandex.find_one({"song-13": {"$exists": "true"}})['song-13']
    yandex15 = yandex.find_one({"song-14": {"$exists": "true"}})['song-14']
    yandex16 = yandex.find_one({"song-15": {"$exists": "true"}})['song-15']
    yandex17 = yandex.find_one({"song-16": {"$exists": "true"}})['song-16']
    yandex18 = yandex.find_one({"song-17": {"$exists": "true"}})['song-17']
    yandex19 = yandex.find_one({"song-18": {"$exists": "true"}})['song-18']
    yandex20 = yandex.find_one({"song-19": {"$exists": "true"}})['song-19']
    yandex21 = yandex.find_one({"song-20": {"$exists": "true"}})['song-20']
    yandex22 = yandex.find_one({"song-21": {"$exists": "true"}})['song-21']
    yandex23 = yandex.find_one({"song-22": {"$exists": "true"}})['song-22']
    yandex24 = yandex.find_one({"song-23": {"$exists": "true"}})['song-23']
    yandex25 = yandex.find_one({"song-24": {"$exists": "true"}})['song-24']
    yandex26 = yandex.find_one({"song-25": {"$exists": "true"}})['song-25']
    yandex27 = yandex.find_one({"song-26": {"$exists": "true"}})['song-26']
    yandex28 = yandex.find_one({"song-27": {"$exists": "true"}})['song-27']
    yandex29 = yandex.find_one({"song-28": {"$exists": "true"}})['song-28']
    yandex30 = yandex.find_one({"song-29": {"$exists": "true"}})['song-29']
    yandex31 = yandex.find_one({"song-30": {"$exists": "true"}})['song-30']
    yandex32 = yandex.find_one({"song-31": {"$exists": "true"}})['song-31']
    yandex33 = yandex.find_one({"song-32": {"$exists": "true"}})['song-32']
    yandex34 = yandex.find_one({"song-33": {"$exists": "true"}})['song-33']
    yandex35 = yandex.find_one({"song-34": {"$exists": "true"}})['song-34']
    yandex36 = yandex.find_one({"song-35": {"$exists": "true"}})['song-35']
    yandex37 = yandex.find_one({"song-36": {"$exists": "true"}})['song-36']
    yandex38 = yandex.find_one({"song-37": {"$exists": "true"}})['song-37']
    yandex39 = yandex.find_one({"song-38": {"$exists": "true"}})['song-38']
    yandex40 = yandex.find_one({"song-39": {"$exists": "true"}})['song-39']
    yandex41 = yandex.find_one({"song-40": {"$exists": "true"}})['song-40']
    yandex42 = yandex.find_one({"song-41": {"$exists": "true"}})['song-41']
    yandex43 = yandex.find_one({"song-42": {"$exists": "true"}})['song-42']
    yandex44 = yandex.find_one({"song-43": {"$exists": "true"}})['song-43']
    yandex45 = yandex.find_one({"song-44": {"$exists": "true"}})['song-44']
    yandex46 = yandex.find_one({"song-45": {"$exists": "true"}})['song-45']
    yandex47 = yandex.find_one({"song-46": {"$exists": "true"}})['song-46']
    yandex48 = yandex.find_one({"song-47": {"$exists": "true"}})['song-47']
    yandex49 = yandex.find_one({"song-48": {"$exists": "true"}})['song-48']
    yandex50 = yandex.find_one({"song-49": {"$exists": "true"}})['song-49']

    return render_template('index.html', data1=f"{artist1} - {song1}", data2=f"{artist2} - {song2}",
                           data3=f"{artist3} - {song3}", data4=f"{artist4} - {song4}", yandex1 = yandex1,
                           yandex2 = yandex2, yandex3 = yandex3, yandex4 = yandex4, yandex5 = yandex5, yandex6 = yandex6
                           , yandex7 = yandex7, yandex8 = yandex8, yandex9 = yandex9, yandex10 = yandex10
                           , yandex11 = yandex11, yandex12 = yandex12, yandex13 = yandex13, yandex14 = yandex14
                           , yandex15 = yandex15, yandex16 = yandex16, yandex17 = yandex17, yandex18 = yandex18
                           , yandex19 = yandex19, yandex20 = yandex20, yandex21 = yandex21, yandex22 = yandex22
                           , yandex23 = yandex23, yandex24 = yandex24, yandex25 = yandex25, yandex26 = yandex26
                           , yandex27 = yandex27, yandex28 = yandex28, yandex29 = yandex29, yandex30 = yandex30
                           , yandex31 = yandex31, yandex32 = yandex32, yandex33 = yandex33, yandex34 = yandex34
                           , yandex35 = yandex35, yandex36 = yandex36, yandex37 = yandex37, yandex38 = yandex38
                           , yandex39 = yandex39, yandex40 = yandex40, yandex41 = yandex41, yandex42 = yandex42
                           , yandex43 = yandex43, yandex44 = yandex44, yandex45 = yandex45, yandex46 = yandex46
                           , yandex47 = yandex47, yandex48 = yandex48, yandex49 = yandex49, yandex50 = yandex50)


@app.route('/filter')
def filter():
    return render_template('filter.html')

if __name__ == "__main__":
    app.run(debug=True) #потом поставить False
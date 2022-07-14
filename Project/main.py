from flask import Flask, render_template
import pymongo
mongo = pymongo.MongoClient()
mydb = mongo["charts"]
mycollection = mydb["spotify"]
app = Flask(__name__)

@app.route('/')
def index():
    artist1 = mycollection.find_one({"artist-0": {"$exists": "true"}})['artist-0']
    song1 = mycollection.find_one({"track-0": {"$exists": "true"}})['track-0']
    artist2 = mycollection.find_one({"artist-1": {"$exists": "true"}})['artist-1']
    song2 = mycollection.find_one({"track-1": {"$exists": "true"}})['track-1']
    artist3 = mycollection.find_one({"artist-2": {"$exists": "true"}})['artist-2']
    song3 = mycollection.find_one({"track-2": {"$exists": "true"}})['track-2']
    artist4 = mycollection.find_one({"artist-3": {"$exists": "true"}})['artist-3']
    song4 = mycollection.find_one({"track-3": {"$exists": "true"}})['track-3']
    return render_template('index.html', data1=f"{artist1} - {song1}", data2=f"{artist2} - {song2}",
                           data3=f"{artist3} - {song3}", data4=f"{artist4} - {song4}")


@app.route('/filter')
def filter():
    return render_template('filter.html')

if __name__ == "__main__":
    app.run(debug=True) #потом поставить False
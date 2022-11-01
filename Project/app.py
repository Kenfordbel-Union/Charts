from flask import Flask, render_template,request, g, abort, flash, redirect, url_for, session
from flask_session import Session
import pymongo
import os
from werkzeug.security import generate_password_hash, check_password_hash
mongo = pymongo.MongoClient()
mydb = mongo["charts"]
#DBs
spotify = mydb["spotify"]
yandex = mydb["yandex"]
youtube = mydb["youtube"]
deezer = mydb["deezer"]
users = mydb["users"]
#app
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'super secret key'


@app.route('/')
def index():
    if session:
        username = session['username']
        logo = os.path.join(r'Project/static/images/logo.png')
# Spotify names/pics/links
        spotify_data = {}
        spotify_pics = {}
        spotify_links = {}
        calc_spotify = 0
# YT names/pics/links
        yt_data = {}
        yt_pics = {}
        yt_links = {}
        calc_yt = 0
# YT names/pics/links
        deezer_data = {}
        deezer_pics = {}
        deezer_links = {}
        calc_deezer = 0
        for i in range(50):
            spotify_data[calc_spotify] = spotify.find_one({f"song-{calc_spotify}":{"$exists": "true"}})[f'song-{calc_spotify}']
            spotify_pics[calc_spotify] = spotify.find_one({f"logo-{calc_spotify}": {"$exists": "true"}})[f'logo-{calc_spotify}']
            spotify_links[calc_spotify] = spotify.find_one({f"sing-{calc_spotify}": {"$exists": "true"}})[f'sing-{calc_spotify}']
            calc_spotify = calc_spotify + 1
        for i in range(40):
            yt_data[calc_yt] = youtube.find_one({f"song-{calc_yt}": {"$exists": "true"}})[f'song-{calc_yt}']
            yt_pics[calc_yt] = youtube.find_one({f"logo-{calc_yt}": {"$exists": "true"}})[f'logo-{calc_yt}']
            yt_links[calc_yt] = youtube.find_one({f"link-{calc_yt}": {"$exists": "true"}})[f'link-{calc_yt}']
            calc_yt = calc_yt + 1
        for i in range(50):
            deezer_data[calc_deezer] = deezer.find_one({f"song-{calc_deezer}": {"$exists": "true"}})[f'song-{calc_deezer}']
            deezer_pics[calc_deezer] = deezer.find_one({f"logo-{calc_deezer}": {"$exists": "true"}})[f'logo-{calc_deezer}']
            deezer_links[calc_deezer] = deezer.find_one({f"sing-{calc_deezer}": {"$exists": "true"}})[f'sing-{calc_deezer}']
            calc_deezer = calc_deezer + 1
        print(deezer_links)

    #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']
    #    yandex2 = yandex.find_one({"song-1": {"$exists": "true"}})['song-1']
    #    yandex3 = yandex.find_one({"song-2": {"$exists": "true"}})['song-2']
    #    yandex4 = yandex.find_one({"song-3": {"$exists": "true"}})['song-3']
    #    yandex5 = yandex.find_one({"song-4": {"$exists": "true"}})['song-4']
    #    yandex6 = yandex.find_one({"song-5": {"$exists": "true"}})['song-5']
    #    yandex7 = yandex.find_one({"song-6": {"$exists": "true"}})['song-6']
    #    yandex8 = yandex.find_one({"song-7": {"$exists": "true"}})['song-7']
    #    yandex9 = yandex.find_one({"song-8": {"$exists": "true"}})['song-8']
    #    yandex10 = yandex.find_one({"song-9": {"$exists": "true"}})['song-9']
    #    yandex11 = yandex.find_one({"song-10": {"$exists": "true"}})['song-10']
    #    yandex12 = yandex.find_one({"song-11": {"$exists": "true"}})['song-11']
    #    yandex13 = yandex.find_one({"song-12": {"$exists": "true"}})['song-12']
    #    yandex14 = yandex.find_one({"song-13": {"$exists": "true"}})['song-13']
    #    yandex15 = yandex.find_one({"song-14": {"$exists": "true"}})['song-14']
    #    yandex16 = yandex.find_one({"song-15": {"$exists": "true"}})['song-15']
    #    yandex17 = yandex.find_one({"song-16": {"$exists": "true"}})['song-16']
    #    yandex18 = yandex.find_one({"song-17": {"$exists": "true"}})['song-17']
    #    yandex19 = yandex.find_one({"song-18": {"$exists": "true"}})['song-18']
    #    yandex20 = yandex.find_one({"song-19": {"$exists": "true"}})['song-19']
    #    yandex21 = yandex.find_one({"song-20": {"$exists": "true"}})['song-20']
    #    yandex22 = yandex.find_one({"song-21": {"$exists": "true"}})['song-21']
    #    yandex23 = yandex.find_one({"song-22": {"$exists": "true"}})['song-22']
    #    yandex24 = yandex.find_one({"song-23": {"$exists": "true"}})['song-23']
    #    yandex25 = yandex.find_one({"song-24": {"$exists": "true"}})['song-24']
    #    yandex26 = yandex.find_one({"song-25": {"$exists": "true"}})['song-25']
    #    yandex27 = yandex.find_one({"song-26": {"$exists": "true"}})['song-26']
    #    yandex28 = yandex.find_one({"song-27": {"$exists": "true"}})['song-27']
    #    yandex29 = yandex.find_one({"song-28": {"$exists": "true"}})['song-28']
    #    yandex30 = yandex.find_one({"song-29": {"$exists": "true"}})['song-29']
    #    yandex31 = yandex.find_one({"song-30": {"$exists": "true"}})['song-30']
    #    yandex32 = yandex.find_one({"song-31": {"$exists": "true"}})['song-31']
    #    yandex33 = yandex.find_one({"song-32": {"$exists": "true"}})['song-32']
    #    yandex34 = yandex.find_one({"song-33": {"$exists": "true"}})['song-33']
    #    yandex35 = yandex.find_one({"song-34": {"$exists": "true"}})['song-34']
    #    yandex36 = yandex.find_one({"song-35": {"$exists": "true"}})['song-35']
    #    yandex37 = yandex.find_one({"song-36": {"$exists": "true"}})['song-36']
    #    yandex38 = yandex.find_one({"song-37": {"$exists": "true"}})['song-37']
    #    yandex39 = yandex.find_one({"song-38": {"$exists": "true"}})['song-38']
    #    yandex40 = yandex.find_one({"song-39": {"$exists": "true"}})['song-39']
    #    yandex41 = yandex.find_one({"song-40": {"$exists": "true"}})['song-40']
    #    yandex42 = yandex.find_one({"song-41": {"$exists": "true"}})['song-41']
    #    yandex43 = yandex.find_one({"song-42": {"$exists": "true"}})['song-42']
    #    yandex44 = yandex.find_one({"song-43": {"$exists": "true"}})['song-43']
    #    yandex45 = yandex.find_one({"song-44": {"$exists": "true"}})['song-44']
    #    yandex46 = yandex.find_one({"song-45": {"$exists": "true"}})['song-45']
    #    yandex47 = yandex.find_one({"song-46": {"$exists": "true"}})['song-46']
    #    yandex48 = yandex.find_one({"song-47": {"$exists": "true"}})['song-47']
    #    yandex49 = yandex.find_one({"song-48": {"$exists": "true"}})['song-48']
    #    yandex50 = yandex.find_one({"song-49": {"$exists": "true"}})['song-49']

        return render_template('index.html', **locals())
    else:
        return redirect(url_for('login'))


@app.route('/filter')
def filter():
    return render_template('filter.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_user = users.find_one({'name': request.form['username']})
        if login_user:
            print(login_user['password'])
            print(check_password_hash(request.form['psw'], login_user['password']))
            if check_password_hash(login_user['password'], request.form['psw']):
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            return 'Invalid username/password combination'
        return 'Invalid username/password combination'
    return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            hashpass = generate_password_hash(request.form['psw'])
            users.insert_one({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'That username already exist!'
    return render_template('register.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=80) #потом поставить False


import pprint

import gridfs
from flask import Flask, render_template, request, g, abort, flash, redirect, url_for, session, send_file
import pymongo
from pymongo import MongoClient
import base64
import os
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
mongo = pymongo.MongoClient()
mydb = mongo["charts"]
#DBs
spotify = mydb["spotify"]
yandex = mydb["yandex"]
youtube = mydb["youtube"]
deezer = mydb["deezer"]
general_chart = mydb["general"]
users = mydb["users"]
fs = gridfs.GridFS(mydb)

#app
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
UPLOAD_FOLDER = r'/static/images/user_pics'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'



@app.route('/welcome')
def welcome():
    return render_template('index_new.html')

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    referer = request.headers.get('Referer')
    if referer != None:
        referer = str(referer.split('/'))
        referer = referer.split()[3]
    if session:
        if 'username' in session:
            region = "Wordwide"
            username = session['username']
            logo = os.path.join(r'Project/static/images/logo.png')
    # Spotify names/pics/links
            spotify_data = {}
            spotify_pics = {}
            spotify_links = {}
            spotify_urls = {}
            calc_spotify = 0
    # YT names/pics/links
            yt_data = {}
            yt_pics = {}
            yt_links = {}
            yt_urls = {}
            calc_yt = 0
    # YT names/pics/links
            deezer_data = {}
            deezer_pics = {}
            deezer_links = {}
            deezer_urls = {}
            calc_deezer = 0
            for i in range(50):
                spotify_data[calc_spotify] = spotify.find_one({f"song-{calc_spotify}":{"$exists": "true"}})[f'song-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"logo-{calc_spotify}": {"$exists": "true"}})[f'logo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"sing-{calc_spotify}": {"$exists": "true"}})[f'sing-{calc_spotify}']
                spotify_urls[calc_spotify] = spotify.find_one({f"url-{calc_spotify}": {"$exists": "true"}})[
                    f'url-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(39):
                yt_data[calc_yt] = youtube.find_one({f"song-{calc_yt}": {"$exists": "true"}})[f'song-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"logo-{calc_yt}": {"$exists": "true"}})[f'logo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"sing-{calc_yt}": {"$exists": "true"}})[f'sing-{calc_yt}']
                yt_urls[calc_yt] = youtube.find_one({f"url-{calc_yt}": {"$exists": "true"}})[f'url-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"song-{calc_deezer}": {"$exists": "true"}})[f'song-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"logo-{calc_deezer}": {"$exists": "true"}})[f'logo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"sing-{calc_deezer}": {"$exists": "true"}})[f'sing-{calc_deezer}']
                deezer_urls[calc_deezer] = deezer.find_one({f"url-{calc_deezer}": {"$exists": "true"}})[f'url-{calc_deezer}']
                calc_deezer = calc_deezer + 1
        #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']
            if "iphone" in user_agent or "android" in user_agent:
                if referer != None:
                    if 'mobile' not in referer:
                        return redirect(url_for('mobile_regions'))
                    else:
                        return render_template('mobile_index_1.html', **locals())
                else:
                    return redirect(url_for('mobile_regions'))
            else:
                return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route('/mobile_regions')
def mobile_regions():
    if 'username' in session:
        username = session['username']
        return render_template('mobile_regions.html', username=username)
    else:
        return redirect(url_for('login'))


@app.route('/regions/ukraine')
def ukraine():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if session:
        if 'username' in session:
            region = "Ukrainian"
            username = session['username']
            logo = os.path.join(r'Project/static/images/logo.png')
            # Spotify names/pics/links
            spotify_data = {}
            spotify_pics = {}
            spotify_links = {}
            spotify_urls = {}
            calc_spotify = 0
            # YT names/pics/links
            yt_data = {}
            yt_pics = {}
            yt_links = {}
            yt_urls = {}
            calc_yt = 0
            # YT names/pics/links
            deezer_data = {}
            deezer_pics = {}
            deezer_links = {}
            deezer_urls = {}
            calc_deezer = 0
            for i in range(50):
                spotify_data[calc_spotify] = spotify.find_one({f"uasong-{calc_spotify}": {"$exists": "true"}})[
                    f'uasong-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"ualogo-{calc_spotify}": {"$exists": "true"}})[
                    f'ualogo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"uasing-{calc_spotify}": {"$exists": "true"}})[
                    f'uasing-{calc_spotify}']
                spotify_urls[calc_spotify] = spotify.find_one({f"uaurl-{calc_spotify}": {"$exists": "true"}})[
                    f'uaurl-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(39):
                yt_data[calc_yt] = youtube.find_one({f"uasong-{calc_yt}": {"$exists": "true"}})[f'uasong-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"ualogo-{calc_yt}": {"$exists": "true"}})[f'ualogo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"uasing-{calc_yt}": {"$exists": "true"}})[
                    f'uasing-{calc_yt}']
                yt_urls[calc_yt] = youtube.find_one({f"uaurl-{calc_yt}": {"$exists": "true"}})[
                    f'uaurl-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"uasong-{calc_deezer}": {"$exists": "true"}})[
                    f'uasong-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"ualogo-{calc_deezer}": {"$exists": "true"}})[
                    f'ualogo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"uasing-{calc_deezer}": {"$exists": "true"}})[
                    f'uasing-{calc_deezer}']
                deezer_urls[calc_deezer] = deezer.find_one({f"uaurl-{calc_deezer}": {"$exists": "true"}})[
                    f'uaurl-{calc_deezer}']
                calc_deezer = calc_deezer + 1
            #
            # #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']

            if "iphone" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            elif "android" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            else:
                return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))


@app.route('/regions/belarus')
def belarus():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if session:
        if 'username' in session:
            region = "Belarusian"
            username = session['username']
            logo = os.path.join(r'Project/static/images/logo.png')
            # Spotify names/pics/links
            spotify_data = {}
            spotify_pics = {}
            spotify_links = {}
            spotify_urls = {}
            calc_spotify = 0
            # YT names/pics/links
            yt_data = {}
            yt_pics = {}
            yt_links = {}
            yt_urls = {}
            calc_yt = 0
            # YT names/pics/links
            deezer_data = {}
            deezer_pics = {}
            deezer_links = {}
            deezer_urls = {}
            calc_deezer = 0
            for i in range(50):
                spotify_data[calc_spotify] = spotify.find_one({f"sbelsong-{calc_spotify}": {"$exists": "true"}})[
                    f'sbelsong-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"sbellogo-{calc_spotify}": {"$exists": "true"}})[
                    f'sbellogo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"sbelsing-{calc_spotify}": {"$exists": "true"}})[
                    f'sbelsing-{calc_spotify}']
                spotify_urls[calc_spotify] = spotify.find_one({f"sbelurl-{calc_spotify}": {"$exists": "true"}})[
                    f'sbelurl-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(39):
                yt_data[calc_yt] = youtube.find_one({f"sbelsong-{calc_yt}": {"$exists": "true"}})[f'sbelsong-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"sbellogo-{calc_yt}": {"$exists": "true"}})[f'sbellogo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"sbelsing-{calc_yt}": {"$exists": "true"}})[f'sbelsing-{calc_yt}']
                yt_urls[calc_yt] = youtube.find_one({f"sbelurl-{calc_yt}": {"$exists": "true"}})[f'sbelurl-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"sbelsong-{calc_deezer}": {"$exists": "true"}})[
                    f'sbelsong-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"sbellogo-{calc_deezer}": {"$exists": "true"}})[
                    f'sbellogo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"sbelsing-{calc_deezer}": {"$exists": "true"}})[
                    f'sbelsing-{calc_deezer}']
                deezer_urls[calc_deezer] = deezer.find_one({f"sbelurl-{calc_deezer}": {"$exists": "true"}})[
                    f'sbelurl-{calc_deezer}']
                calc_deezer = calc_deezer + 1
            #
            # #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']

            if "iphone" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            elif "android" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            else:
                return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))


@app.route('/regions/usa')
def usa():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if session:
        if 'username' in session:
            region = "USA"
            username = session['username']
            logo = os.path.join(r'Project/static/images/logo.png')
            # Spotify names/pics/links
            spotify_data = {}
            spotify_pics = {}
            spotify_links = {}
            spotify_urls = {}
            calc_spotify = 0
            # YT names/pics/links
            yt_data = {}
            yt_pics = {}
            yt_links = {}
            yt_urls = {}
            calc_yt = 0
            # YT names/pics/links
            deezer_data = {}
            deezer_pics = {}
            deezer_links = {}
            deezer_urls = {}
            calc_deezer = 0
            for i in range(50):
                spotify_data[calc_spotify] = spotify.find_one({f"usasong-{calc_spotify}": {"$exists": "true"}})[
                    f'usasong-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"usalogo-{calc_spotify}": {"$exists": "true"}})[
                    f'usalogo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"usasing-{calc_spotify}": {"$exists": "true"}})[
                    f'usasing-{calc_spotify}']
                spotify_urls[calc_spotify] = spotify.find_one({f"usaurl-{calc_spotify}": {"$exists": "true"}})[
                    f'usaurl-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(39):
                yt_data[calc_yt] = youtube.find_one({f"usasong-{calc_yt}": {"$exists": "true"}})[f'usasong-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"usalogo-{calc_yt}": {"$exists": "true"}})[f'usalogo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"usasing-{calc_yt}": {"$exists": "true"}})[
                    f'usasing-{calc_yt}']
                yt_urls[calc_yt] = youtube.find_one({f"usaurl-{calc_yt}": {"$exists": "true"}})[
                    f'usaurl-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"usasong-{calc_deezer}": {"$exists": "true"}})[
                    f'usasong-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"usalogo-{calc_deezer}": {"$exists": "true"}})[
                    f'usalogo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"usasing-{calc_deezer}": {"$exists": "true"}})[
                    f'usasing-{calc_deezer}']
                deezer_urls[calc_deezer] = deezer.find_one({f"usaurl-{calc_deezer}": {"$exists": "true"}})[
                    f'usaurl-{calc_deezer}']
                calc_deezer = calc_deezer + 1
            #
            # #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']

            if "iphone" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            elif "android" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            else:
                return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))


@app.route('/regions/spain')
def spain():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if session:
        if 'username' in session:
            region = "Spanish"
            username = session['username']
            logo = os.path.join(r'Project/static/images/logo.png')
            # Spotify names/pics/links
            spotify_data = {}
            spotify_pics = {}
            spotify_links = {}
            spotify_urls = {}
            calc_spotify = 0
            # YT names/pics/links
            yt_data = {}
            yt_pics = {}
            yt_links = {}
            yt_urls = {}
            calc_yt = 0
            # YT names/pics/links
            deezer_data = {}
            deezer_pics = {}
            deezer_links = {}
            deezer_urls = {}
            calc_deezer = 0
            for i in range(50):
                spotify_data[calc_spotify] = spotify.find_one({f"spasong-{calc_spotify}": {"$exists": "true"}})[
                    f'spasong-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"spalogo-{calc_spotify}": {"$exists": "true"}})[
                    f'spalogo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"spasing-{calc_spotify}": {"$exists": "true"}})[
                    f'spasing-{calc_spotify}']
                spotify_urls[calc_spotify] = spotify.find_one({f"spaurl-{calc_spotify}": {"$exists": "true"}})[
                    f'spaurl-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(39):
                yt_data[calc_yt] = youtube.find_one({f"spasong-{calc_yt}": {"$exists": "true"}})[f'spasong-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"spalogo-{calc_yt}": {"$exists": "true"}})[f'spalogo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"spasing-{calc_yt}": {"$exists": "true"}})[
                    f'spasing-{calc_yt}']
                yt_urls[calc_yt] = youtube.find_one({f"spaurl-{calc_yt}": {"$exists": "true"}})[
                    f'spaurl-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"spasong-{calc_deezer}": {"$exists": "true"}})[
                    f'spasong-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"spalogo-{calc_deezer}": {"$exists": "true"}})[
                    f'spalogo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"spasing-{calc_deezer}": {"$exists": "true"}})[
                    f'spasing-{calc_deezer}']
                deezer_urls[calc_deezer] = deezer.find_one({f"spaurl-{calc_deezer}": {"$exists": "true"}})[
                    f'spaurl-{calc_deezer}']
                calc_deezer = calc_deezer + 1
            #
            # #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']

            if "iphone" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            elif "android" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            else:
                return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))


@app.route('/regions/france')
def france():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if session:
        if 'username' in session:
            region = "French"
            username = session['username']
            logo = os.path.join(r'Project/static/images/logo.png')
            # Spotify names/pics/links
            spotify_data = {}
            spotify_pics = {}
            spotify_links = {}
            spotify_urls = {}
            calc_spotify = 0
            # YT names/pics/links
            yt_data = {}
            yt_pics = {}
            yt_links = {}
            yt_urls = {}
            calc_yt = 0
            # YT names/pics/links
            deezer_data = {}
            deezer_pics = {}
            deezer_links = {}
            deezer_urls = {}
            calc_deezer = 0
            for i in range(50):
                spotify_data[calc_spotify] = spotify.find_one({f"sfrasong-{calc_spotify}": {"$exists": "true"}})[
                    f'sfrasong-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"sfralogo-{calc_spotify}": {"$exists": "true"}})[
                    f'sfralogo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"sfrasing-{calc_spotify}": {"$exists": "true"}})[
                    f'sfrasing-{calc_spotify}']
                spotify_urls[calc_spotify] = spotify.find_one({f"sfraurl-{calc_spotify}": {"$exists": "true"}})[
                    f'sfraurl-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(39):
                yt_data[calc_yt] = youtube.find_one({f"sfrasong-{calc_yt}": {"$exists": "true"}})[f'sfrasong-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"sfralogo-{calc_yt}": {"$exists": "true"}})[f'sfralogo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"sfrasing-{calc_yt}": {"$exists": "true"}})[
                    f'sfrasing-{calc_yt}']
                yt_urls[calc_yt] = youtube.find_one({f"sfraurl-{calc_yt}": {"$exists": "true"}})[
                    f'sfraurl-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"sfrasong-{calc_deezer}": {"$exists": "true"}})[
                    f'sfrasong-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"sfralogo-{calc_deezer}": {"$exists": "true"}})[
                    f'sfralogo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"sfrasing-{calc_deezer}": {"$exists": "true"}})[
                    f'sfrasing-{calc_deezer}']
                deezer_urls[calc_deezer] = deezer.find_one({f"sfraurl-{calc_deezer}": {"$exists": "true"}})[
                    f'sfraurl-{calc_deezer}']
                calc_deezer = calc_deezer + 1
            #
            # #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']

            if "iphone" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            elif "android" in user_agent:
                return render_template('mobile_index_1.html', **locals())
            else:
                return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))

@app.route('/general')
def general():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    general_names = {}
    general_pics = {}
    general_links = {}
    general_urls = {}
    calc = 0
    username = session['username']
    region = "General"
    for i in general_chart.find():
        name = list(i.values())[1]
        general_names[calc] = name
        pic = list(i.values())[5]
        general_pics[calc] = pic
        sing = list(i.values())[6]
        general_links[calc] = sing
        url = list(i.values())[7]
        general_urls[calc] = url
        calc += 1
    if "iphone" in user_agent:
        return render_template('general_mobile.html', **locals())
    elif "android" in user_agent:
        return render_template('general_mobile.html', **locals())
    else:
        return render_template('general.html', **locals())

@app.route('/song/<songid>',  methods=["GET", "POST"])
def song(songid):
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    print(request.method, request.form.get('like'), request.form.get('dislike'))
    regions = ["uaurl", "url", "sfraurl", "spaurl", "usaurl", "sbelurl"]
    if request.method == "GET":
        for j in regions:
            calc = 0
            for i in range(50):
                a = spotify.find_one({f"{j}-{calc}": songid})
                c = deezer.find_one({f"{j}-{calc}": songid})
                yt = youtube.find_one({f"{j}-{calc}": songid})
                if a != None:
                    del a['_id']
                    del a['lastModified']
                    name = list(a.values())[0]
                    likes = list(a.values())[2]
                    logo = list(a.values())[3]
                    sing = list(a.values())[4]
                    comments = list(a.values())[6]
                    if "iphone" in user_agent:
                        return render_template('song_mobile.html', name=name, logo=logo, sing=sing, likes=likes, variable=comments)
                    elif "android" in user_agent:
                        return render_template('song_mobile.html', name=name, logo=logo, sing=sing, likes=likes, variable=comments)
                    else:
                        return render_template('song.html', name=name, logo=logo, sing=sing, likes=likes, variable=comments)

                elif c != None:
                    del c['_id']
                    del c['lastModified']
                    name = list(c.values())[0]
                    likes = list(c.values())[2]
                    logo = list(c.values())[3]
                    sing = list(c.values())[4]
                    comments = list(c.values())[6]
                    print(likes)
                    if "iphone" in user_agent:
                        return render_template('song_mobile.html', name=name, logo=logo, sing=sing, likes=likes,
                                               variable=comments)
                    elif "android" in user_agent:
                        return render_template('song_mobile.html', name=name, logo=logo, sing=sing, likes=likes,
                                               variable=comments)
                    else:
                        return render_template('song.html', name=name, logo=logo, sing=sing, likes=likes,
                                               variable=comments)
                elif yt != None:
                    del yt['_id']
                    del yt['lastModified']
                    name = list(yt.values())[0]
                    likes = list(yt.values())[1]
                    sing = list(yt.values())[3]
                    sing = sing.replace("music", "www")
                    sing = sing.replace("watch?v=", "embed/")
                    comments = list(yt.values())[5]
                    if "iphone" in user_agent:
                        return render_template('song_yt_mobile.html', name=name, sing=sing, likes=likes, variable=comments)
                    elif "android" in user_agent:
                        return render_template('song_yt_mobile.html', name=name, sing=sing, likes=likes, variable=comments)
                    else:
                        return render_template('song_yt.html', name=name, sing=sing, likes=likes, variable=comments)
                calc = calc + 1
    if request.method == "POST" and request.form.get('like') == 'Like':
        for j in regions:
            calc = 0
            for i in range(50):
                b = spotify.find_one({f"{j}-{calc}": songid})
                d = deezer.find_one({f"{j}-{calc}": songid})
                yt = youtube.find_one({f"{j}-{calc}": songid})
                if b != None:
                    del b['_id']
                    del b['lastModified']
                    name = list(b.values())[0]
                    likes = list(b.values())[2]
                    logo = list(b.values())[3]
                    sing = list(b.values())[4]
                    like = spotify.update_one(
                        {f"{j}-{calc}": songid},
                        {
                            "$inc": {
                                f"likes": +1
                            }
                        }
                    )
                    likes = int(likes) + 1
                    return redirect(f"/song/{songid}")
                elif d != None:
                    del d['_id']
                    del d['lastModified']
                    name = list(d.values())[0]
                    likes = list(d.values())[2]
                    logo = list(d.values())[3]
                    sing = list(d.values())[4]
                    like = deezer.update_one(
                        {f"{j}-{calc}": songid},
                        {
                            "$inc": {
                                f"likes": +1
                            }
                        }
                    )
                    likes = int(likes) + 1
                    return redirect(f"/song/{songid}")
                elif yt != None:
                    del yt['_id']
                    del yt['lastModified']
                    name = list(yt.values())[0]
                    likes = list(yt.values())[1]
                    sing = list(yt.values())[3]
                    sing = sing.replace("music", "www")
                    sing = sing.replace("watch?v=", "embed/")
                    like = youtube.update_one(
                        {f"{j}-{calc}": songid},
                        {
                            "$inc": {
                                f"likes": +1
                            }
                        }
                    )
                    return redirect(f"/song/{songid}")
                calc = calc + 1
    if request.method == "POST" and request.form.get('dislike') == 'Dislike':
        for j in regions:
            calc = 0
            for i in range(50):
                b = spotify.find_one({f"{j}-{calc}": songid})
                d = deezer.find_one({f"{j}-{calc}": songid})
                yt = youtube.find_one({f"{j}-{calc}": songid})
                if b != None:
                    del b['_id']
                    del b['lastModified']
                    name = list(b.values())[0]
                    likes = list(b.values())[2]
                    logo = list(b.values())[3]
                    sing = list(b.values())[4]
                    like = spotify.update_one(
                        {f"{j}-{calc}": songid},
                        {
                            "$inc": {
                                f"likes": -1
                            }
                        }
                    )
                    likes = int(likes) - 1
                    return redirect(f"/song/{songid}")
                if d != None:
                    del d['_id']
                    del d['lastModified']
                    name = list(d.values())[0]
                    likes = list(d.values())[2]
                    logo = list(d.values())[3]
                    sing = list(d.values())[4]
                    like = deezer.update_one(
                        {f"{j}-{calc}": songid},
                        {
                            "$inc": {
                                f"likes": -1
                            }
                        }
                    )
                    likes = int(likes) - 1
                    return redirect(f"/song/{songid}")
                elif yt != None:
                    del yt['_id']
                    del yt['lastModified']
                    name = list(yt.values())[0]
                    likes = list(yt.values())[1]
                    sing = list(yt.values())[3]
                    sing = sing.replace("music", "www")
                    sing = sing.replace("watch?v=", "embed/")
                    like = youtube.update_one(
                        {f"{j}-{calc}": songid},
                        {
                            "$inc": {
                                f"likes": -1
                            }
                        }
                    )
                    return redirect(f"/song/{songid}")
                calc = calc + 1
    if request.method == "POST" and request.form.get('submit') == 'submit':
        for j in regions:
            calc = 0
            for i in range(50):
                b = spotify.find_one({f"{j}-{calc}": songid})
                d = deezer.find_one({f"{j}-{calc}": songid})
                yt = youtube.find_one({f"{j}-{calc}": songid})
                if b != None:
                    comments = spotify.update_one(
                        {f"{j}-{calc}": songid},
                        {
                            "$push": {
                                f"xcomments": f"{session['username']} - {request.form['comment']}"
                            }
                        }
                    )
                    return redirect(f"/song/{songid}")
                if d != None:
                    comments = deezer.update_one(
                        {f"{j}-{calc}": songid},
                        {
                            "$push": {
                                f"xcomments": f"{session['username']} - {request.form['comment']}"
                            }
                        }
                    )
                    return redirect(f"/song/{songid}")
                if yt != None:
                    comments = youtube.update_one(
                        {f"{j}-{calc}": songid},
                        {
                            "$push": {
                                f"xcomments": f"{session['username']} - {request.form['comment']}"
                            }
                        }
                    )
                    return redirect(f"/song/{songid}")
                calc = calc + 1


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
            file = request.files['file']
            filename = f"{request.form['username']}.jpg"
            file.save(os.path.join('static/images/user_pics', filename))


            users.insert_one({'name' : request.form['username'], 'password': hashpass, 'real_name': request.form['name'],
                              'surname': request.form['surname'], 'email': request.form['email']})

            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'That username already exist!'
    return render_template('register.html')


@app.route('/logout', methods=["POST", "GET"])
def logout():
    session.pop('username', None)
    flash("Вы вышли из аккаунта", "success")
    print(session)
    return redirect(url_for('login'))

@app.route('/profile', methods=["POST", "GET"])
def profile():
    username = session['username']
    needed_user = users.find_one({'name': username})
    legal_name = needed_user['real_name'] + ' ' + needed_user['surname']
    email = needed_user['email']
    avatar_link = fr'/static/images/user_pics/{username}.jpg'
    print(avatar_link)
    return render_template('profile.html', username=username, legal_name=legal_name, email=email, avatar_link=avatar_link)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=80) #потом поставить False


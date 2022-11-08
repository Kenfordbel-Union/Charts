import pprint

from flask import Flask, render_template,request, g, abort, flash, redirect, url_for, session
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
general_chart = mydb["general"]
users = mydb["users"]
#app
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'super secret key'

@app.route('/')
def index():
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
            for i in range(40):
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
            return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route('/regions/ukraine')
def ukraine():
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
            for i in range(40):
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

            return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))


@app.route('/regions/usa')
def usa():
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
            for i in range(40):
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

            return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))


@app.route('/regions/spain')
def spain():
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
            for i in range(40):
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

            return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))


@app.route('/regions/france')
def france():
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
            for i in range(40):
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
            print(yt_urls)
            #
            # #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']

            return render_template('index.html', **locals())
        else:
            return redirect(url_for('login'))

@app.route('/general')
def general():
    general_names = {}
    general_pics = {}
    general_links = {}
    general_urls = {}
    calc = 0
    username = session['username']
    region = "Worldwide general"
    for i in general_chart.find():
        name = list(i.values())[1]
        general_names[calc] = name
        pic = list(i.values())[4]
        general_pics[calc] = pic
        sing = list(i.values())[5]
        general_links[calc] = sing
        url = list(i.values())[6]
        general_urls[calc] = url
        calc += 1
    print(general_links)

    return render_template('general.html', **locals())

@app.route('/song/<songid>',  methods=["GET", "POST"])
def song(songid):
    print(request.method, request.form.get('like'), request.form.get('dislike'))
    regions = ["uaurl", "url", "sfraurl", "spaurl", "usaurl"]
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
                    likes = list(a.values())[1]
                    logo = list(a.values())[2]
                    sing = list(a.values())[3]
                    comments = list(a.values())[5]
                    print(likes)
                    return render_template('song.html', name=name, logo=logo, sing=sing, likes=likes, variable=comments)
                elif c != None:
                    del c['_id']
                    del c['lastModified']
                    name = list(c.values())[0]
                    likes = list(c.values())[1]
                    logo = list(c.values())[2]
                    sing = list(c.values())[3]
                    comments = list(c.values())[5]
                    print(likes)
                    return render_template('song.html', name=name, logo=logo, sing=sing, likes=likes, variable=comments)
                elif yt != None:
                    del yt['_id']
                    del yt['lastModified']
                    name = list(yt.values())[0]
                    likes = list(yt.values())[1]
                    sing = list(yt.values())[3]
                    sing = sing.replace("music", "www")
                    sing = sing.replace("watch?v=", "embed/")
                    comments = list(yt.values())[5]
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
                    likes = list(b.values())[1]
                    logo = list(b.values())[2]
                    sing = list(b.values())[3]
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
                    likes = list(d.values())[1]
                    logo = list(d.values())[2]
                    sing = list(d.values())[3]
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
                    likes = list(b.values())[1]
                    logo = list(b.values())[2]
                    sing = list(b.values())[3]
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
                    likes = list(d.values())[1]
                    logo = list(d.values())[2]
                    sing = list(d.values())[3]
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
            users.insert_one({'name' : request.form['username'], 'password': hashpass})
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
    return render_template('profile.html', username=username)
    # return f"""<p><a href="{url_for('logout')}">Выйти из профиля</a><p>user info: {session['username']}"""

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=80) #потом поставить False


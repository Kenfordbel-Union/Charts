from flask import Flask, render_template,request, g, abort, flash, redirect, url_for, session
from flask_login import LoginManager
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
        if 'username' in session:
            region = "Wordwide"
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

        #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']

            return render_template('index.html', **locals())
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
                spotify_data[calc_spotify] = spotify.find_one({f"uasong-{calc_spotify}": {"$exists": "true"}})[
                    f'uasong-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"ualogo-{calc_spotify}": {"$exists": "true"}})[
                    f'ualogo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"uasing-{calc_spotify}": {"$exists": "true"}})[
                    f'uasing-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(40):
                yt_data[calc_yt] = youtube.find_one({f"uasong-{calc_yt}": {"$exists": "true"}})[f'uasong-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"ualogo-{calc_yt}": {"$exists": "true"}})[f'ualogo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"ualink-{calc_yt}": {"$exists": "true"}})[
                    f'ualink-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"uasong-{calc_deezer}": {"$exists": "true"}})[
                    f'uasong-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"ualogo-{calc_deezer}": {"$exists": "true"}})[
                    f'ualogo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"uasing-{calc_deezer}": {"$exists": "true"}})[
                    f'uasing-{calc_deezer}']
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
                spotify_data[calc_spotify] = spotify.find_one({f"usasong-{calc_spotify}": {"$exists": "true"}})[
                    f'usasong-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"usalogo-{calc_spotify}": {"$exists": "true"}})[
                    f'usalogo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"usasing-{calc_spotify}": {"$exists": "true"}})[
                    f'usasing-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(40):
                yt_data[calc_yt] = youtube.find_one({f"usasong-{calc_yt}": {"$exists": "true"}})[f'usasong-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"usalogo-{calc_yt}": {"$exists": "true"}})[f'usalogo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"usalink-{calc_yt}": {"$exists": "true"}})[
                    f'usalink-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"usasong-{calc_deezer}": {"$exists": "true"}})[
                    f'usasong-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"usalogo-{calc_deezer}": {"$exists": "true"}})[
                    f'usalogo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"usasing-{calc_deezer}": {"$exists": "true"}})[
                    f'usasing-{calc_deezer}']
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
                spotify_data[calc_spotify] = spotify.find_one({f"spasong-{calc_spotify}": {"$exists": "true"}})[
                    f'spasong-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"spalogo-{calc_spotify}": {"$exists": "true"}})[
                    f'spalogo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"spasing-{calc_spotify}": {"$exists": "true"}})[
                    f'spasing-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(40):
                yt_data[calc_yt] = youtube.find_one({f"spasong-{calc_yt}": {"$exists": "true"}})[f'spasong-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"spalogo-{calc_yt}": {"$exists": "true"}})[f'spalogo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"spalink-{calc_yt}": {"$exists": "true"}})[
                    f'spalink-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"spasong-{calc_deezer}": {"$exists": "true"}})[
                    f'spasong-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"spalogo-{calc_deezer}": {"$exists": "true"}})[
                    f'spalogo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"spasing-{calc_deezer}": {"$exists": "true"}})[
                    f'spasing-{calc_deezer}']
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
                spotify_data[calc_spotify] = spotify.find_one({f"frasong-{calc_spotify}": {"$exists": "true"}})[
                    f'frasong-{calc_spotify}']
                spotify_pics[calc_spotify] = spotify.find_one({f"fralogo-{calc_spotify}": {"$exists": "true"}})[
                    f'fralogo-{calc_spotify}']
                spotify_links[calc_spotify] = spotify.find_one({f"frasing-{calc_spotify}": {"$exists": "true"}})[
                    f'frasing-{calc_spotify}']
                calc_spotify = calc_spotify + 1
            for i in range(40):
                yt_data[calc_yt] = youtube.find_one({f"frasong-{calc_yt}": {"$exists": "true"}})[f'frasong-{calc_yt}']
                yt_pics[calc_yt] = youtube.find_one({f"fralogo-{calc_yt}": {"$exists": "true"}})[f'fralogo-{calc_yt}']
                yt_links[calc_yt] = youtube.find_one({f"fralink-{calc_yt}": {"$exists": "true"}})[
                    f'fralink-{calc_yt}']
                calc_yt = calc_yt + 1
            for i in range(50):
                deezer_data[calc_deezer] = deezer.find_one({f"frasong-{calc_deezer}": {"$exists": "true"}})[
                    f'frasong-{calc_deezer}']
                deezer_pics[calc_deezer] = deezer.find_one({f"fralogo-{calc_deezer}": {"$exists": "true"}})[
                    f'fralogo-{calc_deezer}']
                deezer_links[calc_deezer] = deezer.find_one({f"frasing-{calc_deezer}": {"$exists": "true"}})[
                    f'frasing-{calc_deezer}']
                calc_deezer = calc_deezer + 1
            #
            # #    yandex1 = yandex.find_one({"song-0": {"$exists": "true"}})['song-0']

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


from flask import Flask, render_template
import pymongo
import os
mongo = pymongo.MongoClient()
mydb = mongo["charts"]

spotify = mydb["spotify"]
yandex = mydb["yandex"]
youtube = mydb["youtube"]
deezer = mydb["deezer"]

app = Flask(__name__)

@app.route('/')
def index():
    logo = os.path.join(r'Project/static/images/logo.png')

    spotify1 = spotify.find_one({"song-0": {"$exists": "true"}})['song-0']
    spotify2 = spotify.find_one({"song-1": {"$exists": "true"}})['song-1']
    spotify3 = spotify.find_one({"song-2": {"$exists": "true"}})['song-2']
    spotify4 = spotify.find_one({"song-3": {"$exists": "true"}})['song-3']
    spotify5 = spotify.find_one({"song-4": {"$exists": "true"}})['song-4']
    spotify6 = spotify.find_one({"song-5": {"$exists": "true"}})['song-5']
    spotify7 = spotify.find_one({"song-6": {"$exists": "true"}})['song-6']
    spotify8 = spotify.find_one({"song-7": {"$exists": "true"}})['song-7']
    spotify9 = spotify.find_one({"song-8": {"$exists": "true"}})['song-8']
    spotify10 = spotify.find_one({"song-9": {"$exists": "true"}})['song-9']
    spotify11 = spotify.find_one({"song-10": {"$exists": "true"}})['song-10']
    spotify12 = spotify.find_one({"song-11": {"$exists": "true"}})['song-11']
    spotify13 = spotify.find_one({"song-12": {"$exists": "true"}})['song-12']
    spotify14 = spotify.find_one({"song-13": {"$exists": "true"}})['song-13']
    spotify15 = spotify.find_one({"song-14": {"$exists": "true"}})['song-14']
    spotify16 = spotify.find_one({"song-15": {"$exists": "true"}})['song-15']
    spotify17 = spotify.find_one({"song-16": {"$exists": "true"}})['song-16']
    spotify18 = spotify.find_one({"song-17": {"$exists": "true"}})['song-17']
    spotify19 = spotify.find_one({"song-18": {"$exists": "true"}})['song-18']
    spotify20 = spotify.find_one({"song-19": {"$exists": "true"}})['song-19']
    spotify21 = spotify.find_one({"song-20": {"$exists": "true"}})['song-20']
    spotify22 = spotify.find_one({"song-21": {"$exists": "true"}})['song-21']
    spotify23 = spotify.find_one({"song-22": {"$exists": "true"}})['song-22']
    spotify24 = spotify.find_one({"song-23": {"$exists": "true"}})['song-23']
    spotify25 = spotify.find_one({"song-24": {"$exists": "true"}})['song-24']
    spotify26 = spotify.find_one({"song-25": {"$exists": "true"}})['song-25']
    spotify27 = spotify.find_one({"song-26": {"$exists": "true"}})['song-26']
    spotify28 = spotify.find_one({"song-27": {"$exists": "true"}})['song-27']
    spotify29 = spotify.find_one({"song-28": {"$exists": "true"}})['song-28']
    spotify30 = spotify.find_one({"song-29": {"$exists": "true"}})['song-29']
    spotify31 = spotify.find_one({"song-30": {"$exists": "true"}})['song-30']
    spotify32 = spotify.find_one({"song-31": {"$exists": "true"}})['song-31']
    spotify33 = spotify.find_one({"song-32": {"$exists": "true"}})['song-32']
    spotify34 = spotify.find_one({"song-33": {"$exists": "true"}})['song-33']
    spotify35 = spotify.find_one({"song-34": {"$exists": "true"}})['song-34']
    spotify36 = spotify.find_one({"song-35": {"$exists": "true"}})['song-35']
    spotify37 = spotify.find_one({"song-36": {"$exists": "true"}})['song-36']
    spotify38 = spotify.find_one({"song-37": {"$exists": "true"}})['song-37']
    spotify39 = spotify.find_one({"song-38": {"$exists": "true"}})['song-38']
    spotify40 = spotify.find_one({"song-39": {"$exists": "true"}})['song-39']
    spotify41 = spotify.find_one({"song-40": {"$exists": "true"}})['song-40']
    spotify42 = spotify.find_one({"song-41": {"$exists": "true"}})['song-41']
    spotify43 = spotify.find_one({"song-42": {"$exists": "true"}})['song-42']
    spotify44 = spotify.find_one({"song-43": {"$exists": "true"}})['song-43']
    spotify45 = spotify.find_one({"song-44": {"$exists": "true"}})['song-44']
    spotify46 = spotify.find_one({"song-45": {"$exists": "true"}})['song-45']
    spotify47 = spotify.find_one({"song-46": {"$exists": "true"}})['song-46']
    spotify48 = spotify.find_one({"song-47": {"$exists": "true"}})['song-47']
    spotify49 = spotify.find_one({"song-48": {"$exists": "true"}})['song-48']
    spotify50 = spotify.find_one({"song-49": {"$exists": "true"}})['song-49']

    spotify_pic1 = spotify.find_one({"logo-0": {"$exists": "true"}})['logo-0']
    spotify_pic2 = spotify.find_one({"logo-1": {"$exists": "true"}})['logo-1']
    spotify_pic3 = spotify.find_one({"logo-2": {"$exists": "true"}})['logo-2']
    spotify_pic4 = spotify.find_one({"logo-3": {"$exists": "true"}})['logo-3']
    spotify_pic5 = spotify.find_one({"logo-4": {"$exists": "true"}})['logo-4']
    spotify_pic6 = spotify.find_one({"logo-5": {"$exists": "true"}})['logo-5']
    spotify_pic7 = spotify.find_one({"logo-6": {"$exists": "true"}})['logo-6']
    spotify_pic8 = spotify.find_one({"logo-7": {"$exists": "true"}})['logo-7']
    spotify_pic9 = spotify.find_one({"logo-8": {"$exists": "true"}})['logo-8']
    spotify_pic10 = spotify.find_one({"logo-9": {"$exists": "true"}})['logo-9']
    spotify_pic11 = spotify.find_one({"logo-10": {"$exists": "true"}})['logo-10']
    spotify_pic12 = spotify.find_one({"logo-11": {"$exists": "true"}})['logo-11']
    spotify_pic13 = spotify.find_one({"logo-12": {"$exists": "true"}})['logo-12']
    spotify_pic14 = spotify.find_one({"logo-13": {"$exists": "true"}})['logo-13']
    spotify_pic15 = spotify.find_one({"logo-14": {"$exists": "true"}})['logo-14']
    spotify_pic16 = spotify.find_one({"logo-15": {"$exists": "true"}})['logo-15']
    spotify_pic17 = spotify.find_one({"logo-16": {"$exists": "true"}})['logo-16']
    spotify_pic18 = spotify.find_one({"logo-17": {"$exists": "true"}})['logo-17']
    spotify_pic19 = spotify.find_one({"logo-18": {"$exists": "true"}})['logo-18']
    spotify_pic20 = spotify.find_one({"logo-19": {"$exists": "true"}})['logo-19']
    spotify_pic21 = spotify.find_one({"logo-20": {"$exists": "true"}})['logo-20']
    spotify_pic22 = spotify.find_one({"logo-21": {"$exists": "true"}})['logo-21']
    spotify_pic23 = spotify.find_one({"logo-22": {"$exists": "true"}})['logo-22']
    spotify_pic24 = spotify.find_one({"logo-23": {"$exists": "true"}})['logo-23']
    spotify_pic25 = spotify.find_one({"logo-24": {"$exists": "true"}})['logo-24']
    spotify_pic26 = spotify.find_one({"logo-25": {"$exists": "true"}})['logo-25']
    spotify_pic27 = spotify.find_one({"logo-26": {"$exists": "true"}})['logo-26']
    spotify_pic28 = spotify.find_one({"logo-27": {"$exists": "true"}})['logo-27']
    spotify_pic29 = spotify.find_one({"logo-28": {"$exists": "true"}})['logo-28']
    spotify_pic30 = spotify.find_one({"logo-29": {"$exists": "true"}})['logo-29']
    spotify_pic31 = spotify.find_one({"logo-30": {"$exists": "true"}})['logo-30']
    spotify_pic32 = spotify.find_one({"logo-31": {"$exists": "true"}})['logo-31']
    spotify_pic33 = spotify.find_one({"logo-32": {"$exists": "true"}})['logo-32']
    spotify_pic34 = spotify.find_one({"logo-33": {"$exists": "true"}})['logo-33']
    spotify_pic35 = spotify.find_one({"logo-34": {"$exists": "true"}})['logo-34']
    spotify_pic36 = spotify.find_one({"logo-35": {"$exists": "true"}})['logo-35']
    spotify_pic37 = spotify.find_one({"logo-36": {"$exists": "true"}})['logo-36']
    spotify_pic38 = spotify.find_one({"logo-37": {"$exists": "true"}})['logo-37']
    spotify_pic39 = spotify.find_one({"logo-38": {"$exists": "true"}})['logo-38']
    spotify_pic40 = spotify.find_one({"logo-39": {"$exists": "true"}})['logo-39']
    spotify_pic41 = spotify.find_one({"logo-40": {"$exists": "true"}})['logo-40']
    spotify_pic42 = spotify.find_one({"logo-41": {"$exists": "true"}})['logo-41']
    spotify_pic43 = spotify.find_one({"logo-42": {"$exists": "true"}})['logo-42']
    spotify_pic44 = spotify.find_one({"logo-43": {"$exists": "true"}})['logo-43']
    spotify_pic45 = spotify.find_one({"logo-44": {"$exists": "true"}})['logo-44']
    spotify_pic46 = spotify.find_one({"logo-45": {"$exists": "true"}})['logo-45']
    spotify_pic47 = spotify.find_one({"logo-46": {"$exists": "true"}})['logo-46']
    spotify_pic48 = spotify.find_one({"logo-47": {"$exists": "true"}})['logo-47']
    spotify_pic49 = spotify.find_one({"logo-48": {"$exists": "true"}})['logo-48']
    spotify_pic50 = spotify.find_one({"logo-49": {"$exists": "true"}})['logo-49']

    spotify_sing1 = spotify.find_one({"sing-0": {"$exists": "true"}})['sing-0']
    spotify_sing2 = spotify.find_one({"sing-1": {"$exists": "true"}})['sing-1']
    spotify_sing3 = spotify.find_one({"sing-2": {"$exists": "true"}})['sing-2']
    spotify_sing4 = spotify.find_one({"sing-3": {"$exists": "true"}})['sing-3']
    spotify_sing5 = spotify.find_one({"sing-4": {"$exists": "true"}})['sing-4']
    spotify_sing6 = spotify.find_one({"sing-5": {"$exists": "true"}})['sing-5']
    spotify_sing7 = spotify.find_one({"sing-6": {"$exists": "true"}})['sing-6']
    spotify_sing8 = spotify.find_one({"sing-7": {"$exists": "true"}})['sing-7']
    spotify_sing9 = spotify.find_one({"sing-8": {"$exists": "true"}})['sing-8']
    spotify_sing10 = spotify.find_one({"sing-9": {"$exists": "true"}})['sing-9']
    spotify_sing11 = spotify.find_one({"sing-10": {"$exists": "true"}})['sing-10']
    spotify_sing12 = spotify.find_one({"sing-11": {"$exists": "true"}})['sing-11']
    spotify_sing13 = spotify.find_one({"sing-12": {"$exists": "true"}})['sing-12']
    spotify_sing14 = spotify.find_one({"sing-13": {"$exists": "true"}})['sing-13']
    spotify_sing15 = spotify.find_one({"sing-14": {"$exists": "true"}})['sing-14']
    spotify_sing16 = spotify.find_one({"sing-15": {"$exists": "true"}})['sing-15']
    spotify_sing17 = spotify.find_one({"sing-16": {"$exists": "true"}})['sing-16']
    spotify_sing18 = spotify.find_one({"sing-17": {"$exists": "true"}})['sing-17']
    spotify_sing19 = spotify.find_one({"sing-18": {"$exists": "true"}})['sing-18']
    spotify_sing20 = spotify.find_one({"sing-19": {"$exists": "true"}})['sing-19']
    spotify_sing21 = spotify.find_one({"sing-20": {"$exists": "true"}})['sing-20']
    spotify_sing22 = spotify.find_one({"sing-21": {"$exists": "true"}})['sing-21']
    spotify_sing23 = spotify.find_one({"sing-22": {"$exists": "true"}})['sing-22']
    spotify_sing24 = spotify.find_one({"sing-23": {"$exists": "true"}})['sing-23']
    spotify_sing25 = spotify.find_one({"sing-24": {"$exists": "true"}})['sing-24']
    spotify_sing26 = spotify.find_one({"sing-25": {"$exists": "true"}})['sing-25']
    spotify_sing27 = spotify.find_one({"sing-26": {"$exists": "true"}})['sing-26']
    spotify_sing28 = spotify.find_one({"sing-27": {"$exists": "true"}})['sing-27']
    spotify_sing29 = spotify.find_one({"sing-28": {"$exists": "true"}})['sing-28']
    spotify_sing30 = spotify.find_one({"sing-29": {"$exists": "true"}})['sing-29']
    spotify_sing31 = spotify.find_one({"sing-30": {"$exists": "true"}})['sing-30']
    spotify_sing32 = spotify.find_one({"sing-31": {"$exists": "true"}})['sing-31']
    spotify_sing33 = spotify.find_one({"sing-32": {"$exists": "true"}})['sing-32']
    spotify_sing34 = spotify.find_one({"sing-33": {"$exists": "true"}})['sing-33']
    spotify_sing35 = spotify.find_one({"sing-34": {"$exists": "true"}})['sing-34']
    spotify_sing36 = spotify.find_one({"sing-35": {"$exists": "true"}})['sing-35']
    spotify_sing37 = spotify.find_one({"sing-36": {"$exists": "true"}})['sing-36']
    spotify_sing38 = spotify.find_one({"sing-37": {"$exists": "true"}})['sing-37']
    spotify_sing39 = spotify.find_one({"sing-38": {"$exists": "true"}})['sing-38']
    spotify_sing40 = spotify.find_one({"sing-39": {"$exists": "true"}})['sing-39']
    spotify_sing41 = spotify.find_one({"sing-40": {"$exists": "true"}})['sing-40']
    spotify_sing42 = spotify.find_one({"sing-41": {"$exists": "true"}})['sing-41']
    spotify_sing43 = spotify.find_one({"sing-42": {"$exists": "true"}})['sing-42']
    spotify_sing44 = spotify.find_one({"sing-43": {"$exists": "true"}})['sing-43']
    spotify_sing45 = spotify.find_one({"sing-44": {"$exists": "true"}})['sing-44']
    spotify_sing46 = spotify.find_one({"sing-45": {"$exists": "true"}})['sing-45']
    spotify_sing47 = spotify.find_one({"sing-46": {"$exists": "true"}})['sing-46']
    spotify_sing48 = spotify.find_one({"sing-47": {"$exists": "true"}})['sing-47']
    spotify_sing49 = spotify.find_one({"sing-48": {"$exists": "true"}})['sing-48']
    spotify_sing50 = spotify.find_one({"sing-49": {"$exists": "true"}})['sing-49']

    youtube1 = youtube.find_one({"song-0": {"$exists": "true"}})['song-0']
    youtube2 = youtube.find_one({"song-1": {"$exists": "true"}})['song-1']
    youtube3 = youtube.find_one({"song-2": {"$exists": "true"}})['song-2']
    youtube4 = youtube.find_one({"song-3": {"$exists": "true"}})['song-3']
    youtube5 = youtube.find_one({"song-4": {"$exists": "true"}})['song-4']
    youtube6 = youtube.find_one({"song-5": {"$exists": "true"}})['song-5']
    youtube7 = youtube.find_one({"song-6": {"$exists": "true"}})['song-6']
    youtube8 = youtube.find_one({"song-7": {"$exists": "true"}})['song-7']
    youtube9 = youtube.find_one({"song-8": {"$exists": "true"}})['song-8']
    youtube10 = youtube.find_one({"song-9": {"$exists": "true"}})['song-9']
    youtube11 = youtube.find_one({"song-10": {"$exists": "true"}})['song-10']
    youtube12 = youtube.find_one({"song-11": {"$exists": "true"}})['song-11']
    youtube13 = youtube.find_one({"song-12": {"$exists": "true"}})['song-12']
    youtube14 = youtube.find_one({"song-13": {"$exists": "true"}})['song-13']
    youtube15 = youtube.find_one({"song-14": {"$exists": "true"}})['song-14']
    youtube16 = youtube.find_one({"song-15": {"$exists": "true"}})['song-15']
    youtube17 = youtube.find_one({"song-16": {"$exists": "true"}})['song-16']
    youtube18 = youtube.find_one({"song-17": {"$exists": "true"}})['song-17']
    youtube19 = youtube.find_one({"song-18": {"$exists": "true"}})['song-18']
    youtube20 = youtube.find_one({"song-19": {"$exists": "true"}})['song-19']
    youtube21 = youtube.find_one({"song-20": {"$exists": "true"}})['song-20']
    youtube22 = youtube.find_one({"song-21": {"$exists": "true"}})['song-21']
    youtube23 = youtube.find_one({"song-22": {"$exists": "true"}})['song-22']
    youtube24 = youtube.find_one({"song-23": {"$exists": "true"}})['song-23']
    youtube25 = youtube.find_one({"song-24": {"$exists": "true"}})['song-24']
    youtube26 = youtube.find_one({"song-25": {"$exists": "true"}})['song-25']
    youtube27 = youtube.find_one({"song-26": {"$exists": "true"}})['song-26']
    youtube28 = youtube.find_one({"song-27": {"$exists": "true"}})['song-27']
    youtube29 = youtube.find_one({"song-28": {"$exists": "true"}})['song-28']
    youtube30 = youtube.find_one({"song-29": {"$exists": "true"}})['song-29']
    youtube31 = youtube.find_one({"song-30": {"$exists": "true"}})['song-30']
    youtube32 = youtube.find_one({"song-31": {"$exists": "true"}})['song-31']
    youtube33 = youtube.find_one({"song-32": {"$exists": "true"}})['song-32']
    youtube34 = youtube.find_one({"song-33": {"$exists": "true"}})['song-33']
    youtube35 = youtube.find_one({"song-34": {"$exists": "true"}})['song-34']
    youtube36 = youtube.find_one({"song-35": {"$exists": "true"}})['song-35']
    youtube37 = youtube.find_one({"song-36": {"$exists": "true"}})['song-36']
    youtube38 = youtube.find_one({"song-37": {"$exists": "true"}})['song-37']
    youtube39 = youtube.find_one({"song-38": {"$exists": "true"}})['song-38']
    youtube40 = youtube.find_one({"song-39": {"$exists": "true"}})['song-39']


    youtube_pic1 = youtube.find_one({"logo-0": {"$exists": "true"}})['logo-0']
    youtube_pic2 = youtube.find_one({"logo-1": {"$exists": "true"}})['logo-1']
    youtube_pic3 = youtube.find_one({"logo-2": {"$exists": "true"}})['logo-2']
    youtube_pic4 = youtube.find_one({"logo-3": {"$exists": "true"}})['logo-3']
    youtube_pic5 = youtube.find_one({"logo-4": {"$exists": "true"}})['logo-4']
    youtube_pic6 = youtube.find_one({"logo-5": {"$exists": "true"}})['logo-5']
    youtube_pic7 = youtube.find_one({"logo-6": {"$exists": "true"}})['logo-6']
    youtube_pic8 = youtube.find_one({"logo-7": {"$exists": "true"}})['logo-7']
    youtube_pic9 = youtube.find_one({"logo-8": {"$exists": "true"}})['logo-8']
    youtube_pic10 = youtube.find_one({"logo-9": {"$exists": "true"}})['logo-9']
    youtube_pic11 = youtube.find_one({"logo-10": {"$exists": "true"}})['logo-10']
    youtube_pic12 = youtube.find_one({"logo-11": {"$exists": "true"}})['logo-11']
    youtube_pic13 = youtube.find_one({"logo-12": {"$exists": "true"}})['logo-12']
    youtube_pic14 = youtube.find_one({"logo-13": {"$exists": "true"}})['logo-13']
    youtube_pic15 = youtube.find_one({"logo-14": {"$exists": "true"}})['logo-14']
    youtube_pic16 = youtube.find_one({"logo-15": {"$exists": "true"}})['logo-15']
    youtube_pic17 = youtube.find_one({"logo-16": {"$exists": "true"}})['logo-16']
    youtube_pic18 = youtube.find_one({"logo-17": {"$exists": "true"}})['logo-17']
    youtube_pic19 = youtube.find_one({"logo-18": {"$exists": "true"}})['logo-18']
    youtube_pic20 = youtube.find_one({"logo-19": {"$exists": "true"}})['logo-19']
    youtube_pic21 = youtube.find_one({"logo-20": {"$exists": "true"}})['logo-20']
    youtube_pic22 = youtube.find_one({"logo-21": {"$exists": "true"}})['logo-21']
    youtube_pic23 = youtube.find_one({"logo-22": {"$exists": "true"}})['logo-22']
    youtube_pic24 = youtube.find_one({"logo-23": {"$exists": "true"}})['logo-23']
    youtube_pic25 = youtube.find_one({"logo-24": {"$exists": "true"}})['logo-24']
    youtube_pic26 = youtube.find_one({"logo-25": {"$exists": "true"}})['logo-25']
    youtube_pic27 = youtube.find_one({"logo-26": {"$exists": "true"}})['logo-26']
    youtube_pic28 = youtube.find_one({"logo-27": {"$exists": "true"}})['logo-27']
    youtube_pic29 = youtube.find_one({"logo-28": {"$exists": "true"}})['logo-28']
    youtube_pic30 = youtube.find_one({"logo-29": {"$exists": "true"}})['logo-29']
    youtube_pic31 = youtube.find_one({"logo-30": {"$exists": "true"}})['logo-30']
    youtube_pic32 = youtube.find_one({"logo-31": {"$exists": "true"}})['logo-31']
    youtube_pic33 = youtube.find_one({"logo-32": {"$exists": "true"}})['logo-32']
    youtube_pic34 = youtube.find_one({"logo-33": {"$exists": "true"}})['logo-33']
    youtube_pic35 = youtube.find_one({"logo-34": {"$exists": "true"}})['logo-34']
    youtube_pic36 = youtube.find_one({"logo-35": {"$exists": "true"}})['logo-35']
    youtube_pic37 = youtube.find_one({"logo-36": {"$exists": "true"}})['logo-36']
    youtube_pic38 = youtube.find_one({"logo-37": {"$exists": "true"}})['logo-37']
    youtube_pic39 = youtube.find_one({"logo-38": {"$exists": "true"}})['logo-38']
    youtube_pic40 = youtube.find_one({"logo-39": {"$exists": "true"}})['logo-39']

    youtube_link1 = youtube.find_one({"link-0": {"$exists": "true"}})['link-0']
    youtube_link2 = youtube.find_one({"link-1": {"$exists": "true"}})['link-1']
    youtube_link3 = youtube.find_one({"link-2": {"$exists": "true"}})['link-2']
    youtube_link4 = youtube.find_one({"link-3": {"$exists": "true"}})['link-3']
    youtube_link5 = youtube.find_one({"link-4": {"$exists": "true"}})['link-4']
    youtube_link6 = youtube.find_one({"link-5": {"$exists": "true"}})['link-5']
    youtube_link7 = youtube.find_one({"link-6": {"$exists": "true"}})['link-6']
    youtube_link8 = youtube.find_one({"link-7": {"$exists": "true"}})['link-7']
    youtube_link9 = youtube.find_one({"link-8": {"$exists": "true"}})['link-8']
    youtube_link10 = youtube.find_one({"link-9": {"$exists": "true"}})['link-9']
    youtube_link11 = youtube.find_one({"link-10": {"$exists": "true"}})['link-10']
    youtube_link12 = youtube.find_one({"link-11": {"$exists": "true"}})['link-11']
    youtube_link13 = youtube.find_one({"link-12": {"$exists": "true"}})['link-12']
    youtube_link14 = youtube.find_one({"link-13": {"$exists": "true"}})['link-13']
    youtube_link15 = youtube.find_one({"link-14": {"$exists": "true"}})['link-14']
    youtube_link16 = youtube.find_one({"link-15": {"$exists": "true"}})['link-15']
    youtube_link17 = youtube.find_one({"link-16": {"$exists": "true"}})['link-16']
    youtube_link18 = youtube.find_one({"link-17": {"$exists": "true"}})['link-17']
    youtube_link19 = youtube.find_one({"link-18": {"$exists": "true"}})['link-18']
    youtube_link20 = youtube.find_one({"link-19": {"$exists": "true"}})['link-19']
    youtube_link21 = youtube.find_one({"link-20": {"$exists": "true"}})['link-20']
    youtube_link22 = youtube.find_one({"link-21": {"$exists": "true"}})['link-21']
    youtube_link23 = youtube.find_one({"link-22": {"$exists": "true"}})['link-22']
    youtube_link24 = youtube.find_one({"link-23": {"$exists": "true"}})['link-23']
    youtube_link25 = youtube.find_one({"link-24": {"$exists": "true"}})['link-24']
    youtube_link26 = youtube.find_one({"link-25": {"$exists": "true"}})['link-25']
    youtube_link27 = youtube.find_one({"link-26": {"$exists": "true"}})['link-26']
    youtube_link28 = youtube.find_one({"link-27": {"$exists": "true"}})['link-27']
    youtube_link29 = youtube.find_one({"link-28": {"$exists": "true"}})['link-28']
    youtube_link30 = youtube.find_one({"link-29": {"$exists": "true"}})['link-29']
    youtube_link31 = youtube.find_one({"link-30": {"$exists": "true"}})['link-30']
    youtube_link32 = youtube.find_one({"link-31": {"$exists": "true"}})['link-31']
    youtube_link33 = youtube.find_one({"link-32": {"$exists": "true"}})['link-32']
    youtube_link34 = youtube.find_one({"link-33": {"$exists": "true"}})['link-33']
    youtube_link35 = youtube.find_one({"link-34": {"$exists": "true"}})['link-34']
    youtube_link36 = youtube.find_one({"link-35": {"$exists": "true"}})['link-35']
    youtube_link37 = youtube.find_one({"link-36": {"$exists": "true"}})['link-36']
    youtube_link38 = youtube.find_one({"link-37": {"$exists": "true"}})['link-37']
    youtube_link39 = youtube.find_one({"link-38": {"$exists": "true"}})['link-38']
    youtube_link40 = youtube.find_one({"link-39": {"$exists": "true"}})['link-39']

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

    deezer1 = deezer.find_one({"song-0": {"$exists": "true"}})['song-0']
    deezer2 = deezer.find_one({"song-1": {"$exists": "true"}})['song-1']
    deezer3 = deezer.find_one({"song-2": {"$exists": "true"}})['song-2']
    deezer4 = deezer.find_one({"song-3": {"$exists": "true"}})['song-3']
    deezer5 = deezer.find_one({"song-4": {"$exists": "true"}})['song-4']
    deezer6 = deezer.find_one({"song-5": {"$exists": "true"}})['song-5']
    deezer7 = deezer.find_one({"song-6": {"$exists": "true"}})['song-6']
    deezer8 = deezer.find_one({"song-7": {"$exists": "true"}})['song-7']
    deezer9 = deezer.find_one({"song-8": {"$exists": "true"}})['song-8']
    deezer10 = deezer.find_one({"song-9": {"$exists": "true"}})['song-9']
    deezer11 = deezer.find_one({"song-10": {"$exists": "true"}})['song-10']
    deezer12 = deezer.find_one({"song-11": {"$exists": "true"}})['song-11']
    deezer13 = deezer.find_one({"song-12": {"$exists": "true"}})['song-12']
    deezer14 = deezer.find_one({"song-13": {"$exists": "true"}})['song-13']
    deezer15 = deezer.find_one({"song-14": {"$exists": "true"}})['song-14']
    deezer16 = deezer.find_one({"song-15": {"$exists": "true"}})['song-15']
    deezer17 = deezer.find_one({"song-16": {"$exists": "true"}})['song-16']
    deezer18 = deezer.find_one({"song-17": {"$exists": "true"}})['song-17']
    deezer19 = deezer.find_one({"song-18": {"$exists": "true"}})['song-18']
    deezer20 = deezer.find_one({"song-19": {"$exists": "true"}})['song-19']
    deezer21 = deezer.find_one({"song-20": {"$exists": "true"}})['song-20']
    deezer22 = deezer.find_one({"song-21": {"$exists": "true"}})['song-21']
    deezer23 = deezer.find_one({"song-22": {"$exists": "true"}})['song-22']
    deezer24 = deezer.find_one({"song-23": {"$exists": "true"}})['song-23']
    deezer25 = deezer.find_one({"song-24": {"$exists": "true"}})['song-24']
    deezer26 = deezer.find_one({"song-25": {"$exists": "true"}})['song-25']
    deezer27 = deezer.find_one({"song-26": {"$exists": "true"}})['song-26']
    deezer28 = deezer.find_one({"song-27": {"$exists": "true"}})['song-27']
    deezer29 = deezer.find_one({"song-28": {"$exists": "true"}})['song-28']
    deezer30 = deezer.find_one({"song-29": {"$exists": "true"}})['song-29']
    deezer31 = deezer.find_one({"song-30": {"$exists": "true"}})['song-30']
    deezer32 = deezer.find_one({"song-31": {"$exists": "true"}})['song-31']
    deezer33 = deezer.find_one({"song-32": {"$exists": "true"}})['song-32']
    deezer34 = deezer.find_one({"song-33": {"$exists": "true"}})['song-33']
    deezer35 = deezer.find_one({"song-34": {"$exists": "true"}})['song-34']
    deezer36 = deezer.find_one({"song-35": {"$exists": "true"}})['song-35']
    deezer37 = deezer.find_one({"song-36": {"$exists": "true"}})['song-36']
    deezer38 = deezer.find_one({"song-37": {"$exists": "true"}})['song-37']
    deezer39 = deezer.find_one({"song-38": {"$exists": "true"}})['song-38']
    deezer40 = deezer.find_one({"song-39": {"$exists": "true"}})['song-39']
    deezer41 = deezer.find_one({"song-40": {"$exists": "true"}})['song-40']
    deezer42 = deezer.find_one({"song-41": {"$exists": "true"}})['song-41']
    deezer43 = deezer.find_one({"song-42": {"$exists": "true"}})['song-42']
    deezer44 = deezer.find_one({"song-43": {"$exists": "true"}})['song-43']
    deezer45 = deezer.find_one({"song-44": {"$exists": "true"}})['song-44']
    deezer46 = deezer.find_one({"song-45": {"$exists": "true"}})['song-45']
    deezer47 = deezer.find_one({"song-46": {"$exists": "true"}})['song-46']
    deezer48 = deezer.find_one({"song-47": {"$exists": "true"}})['song-47']
    deezer49 = deezer.find_one({"song-48": {"$exists": "true"}})['song-48']
    deezer50 = deezer.find_one({"song-49": {"$exists": "true"}})['song-49']

    deezer_sing1 = deezer.find_one({"sing-0": {"$exists": "true"}})['sing-0']
    deezer_sing2 = deezer.find_one({"sing-1": {"$exists": "true"}})['sing-1']
    deezer_sing3 = deezer.find_one({"sing-2": {"$exists": "true"}})['sing-2']
    deezer_sing4 = deezer.find_one({"sing-3": {"$exists": "true"}})['sing-3']
    deezer_sing5 = deezer.find_one({"sing-4": {"$exists": "true"}})['sing-4']
    deezer_sing6 = deezer.find_one({"sing-5": {"$exists": "true"}})['sing-5']
    deezer_sing7 = deezer.find_one({"sing-6": {"$exists": "true"}})['sing-6']
    deezer_sing8 = deezer.find_one({"sing-7": {"$exists": "true"}})['sing-7']
    deezer_sing9 = deezer.find_one({"sing-8": {"$exists": "true"}})['sing-8']
    deezer_sing10 = deezer.find_one({"sing-9": {"$exists": "true"}})['sing-9']
    deezer_sing11 = deezer.find_one({"sing-10": {"$exists": "true"}})['sing-10']
    deezer_sing12 = deezer.find_one({"sing-11": {"$exists": "true"}})['sing-11']
    deezer_sing13 = deezer.find_one({"sing-12": {"$exists": "true"}})['sing-12']
    deezer_sing14 = deezer.find_one({"sing-13": {"$exists": "true"}})['sing-13']
    deezer_sing15 = deezer.find_one({"sing-14": {"$exists": "true"}})['sing-14']
    deezer_sing16 = deezer.find_one({"sing-15": {"$exists": "true"}})['sing-15']
    deezer_sing17 = deezer.find_one({"sing-16": {"$exists": "true"}})['sing-16']
    deezer_sing18 = deezer.find_one({"sing-17": {"$exists": "true"}})['sing-17']
    deezer_sing19 = deezer.find_one({"sing-18": {"$exists": "true"}})['sing-18']
    deezer_sing20 = deezer.find_one({"sing-19": {"$exists": "true"}})['sing-19']
    deezer_sing21 = deezer.find_one({"sing-20": {"$exists": "true"}})['sing-20']
    deezer_sing22 = deezer.find_one({"sing-21": {"$exists": "true"}})['sing-21']
    deezer_sing23 = deezer.find_one({"sing-22": {"$exists": "true"}})['sing-22']
    deezer_sing24 = deezer.find_one({"sing-23": {"$exists": "true"}})['sing-23']
    deezer_sing25 = deezer.find_one({"sing-24": {"$exists": "true"}})['sing-24']
    deezer_sing26 = deezer.find_one({"sing-25": {"$exists": "true"}})['sing-25']
    deezer_sing27 = deezer.find_one({"sing-26": {"$exists": "true"}})['sing-26']
    deezer_sing28 = deezer.find_one({"sing-27": {"$exists": "true"}})['sing-27']
    deezer_sing29 = deezer.find_one({"sing-28": {"$exists": "true"}})['sing-28']
    deezer_sing30 = deezer.find_one({"sing-29": {"$exists": "true"}})['sing-29']
    deezer_sing31 = deezer.find_one({"sing-30": {"$exists": "true"}})['sing-30']
    deezer_sing32 = deezer.find_one({"sing-31": {"$exists": "true"}})['sing-31']
    deezer_sing33 = deezer.find_one({"sing-32": {"$exists": "true"}})['sing-32']
    deezer_sing34 = deezer.find_one({"sing-33": {"$exists": "true"}})['sing-33']
    deezer_sing35 = deezer.find_one({"sing-34": {"$exists": "true"}})['sing-34']
    deezer_sing36 = deezer.find_one({"sing-35": {"$exists": "true"}})['sing-35']
    deezer_sing37 = deezer.find_one({"sing-36": {"$exists": "true"}})['sing-36']
    deezer_sing38 = deezer.find_one({"sing-37": {"$exists": "true"}})['sing-37']
    deezer_sing39 = deezer.find_one({"sing-38": {"$exists": "true"}})['sing-38']
    deezer_sing40 = deezer.find_one({"sing-39": {"$exists": "true"}})['sing-39']
    deezer_sing41 = deezer.find_one({"sing-40": {"$exists": "true"}})['sing-40']
    deezer_sing42 = deezer.find_one({"sing-41": {"$exists": "true"}})['sing-41']
    deezer_sing43 = deezer.find_one({"sing-42": {"$exists": "true"}})['sing-42']
    deezer_sing44 = deezer.find_one({"sing-43": {"$exists": "true"}})['sing-43']
    deezer_sing45 = deezer.find_one({"sing-44": {"$exists": "true"}})['sing-44']
    deezer_sing46 = deezer.find_one({"sing-45": {"$exists": "true"}})['sing-45']
    deezer_sing47 = deezer.find_one({"sing-46": {"$exists": "true"}})['sing-46']
    deezer_sing48 = deezer.find_one({"sing-47": {"$exists": "true"}})['sing-47']
    deezer_sing49 = deezer.find_one({"sing-48": {"$exists": "true"}})['sing-48']
    deezer_sing50 = deezer.find_one({"sing-49": {"$exists": "true"}})['sing-49']

    deezer_pic1 = deezer.find_one({"logo-0": {"$exists": "true"}})['logo-0']
    deezer_pic2 = deezer.find_one({"logo-1": {"$exists": "true"}})['logo-1']
    deezer_pic3 = deezer.find_one({"logo-2": {"$exists": "true"}})['logo-2']
    deezer_pic4 = deezer.find_one({"logo-3": {"$exists": "true"}})['logo-3']
    deezer_pic5 = deezer.find_one({"logo-4": {"$exists": "true"}})['logo-4']
    deezer_pic6 = deezer.find_one({"logo-5": {"$exists": "true"}})['logo-5']
    deezer_pic7 = deezer.find_one({"logo-6": {"$exists": "true"}})['logo-6']
    deezer_pic8 = deezer.find_one({"logo-7": {"$exists": "true"}})['logo-7']
    deezer_pic9 = deezer.find_one({"logo-8": {"$exists": "true"}})['logo-8']
    deezer_pic10 = deezer.find_one({"logo-9": {"$exists": "true"}})['logo-9']
    deezer_pic11 = deezer.find_one({"logo-10": {"$exists": "true"}})['logo-10']
    deezer_pic12 = deezer.find_one({"logo-11": {"$exists": "true"}})['logo-11']
    deezer_pic13 = deezer.find_one({"logo-12": {"$exists": "true"}})['logo-12']
    deezer_pic14 = deezer.find_one({"logo-13": {"$exists": "true"}})['logo-13']
    deezer_pic15 = deezer.find_one({"logo-14": {"$exists": "true"}})['logo-14']
    deezer_pic16 = deezer.find_one({"logo-15": {"$exists": "true"}})['logo-15']
    deezer_pic17 = deezer.find_one({"logo-16": {"$exists": "true"}})['logo-16']
    deezer_pic18 = deezer.find_one({"logo-17": {"$exists": "true"}})['logo-17']
    deezer_pic19 = deezer.find_one({"logo-18": {"$exists": "true"}})['logo-18']
    deezer_pic20 = deezer.find_one({"logo-19": {"$exists": "true"}})['logo-19']
    deezer_pic21 = deezer.find_one({"logo-20": {"$exists": "true"}})['logo-20']
    deezer_pic22 = deezer.find_one({"logo-21": {"$exists": "true"}})['logo-21']
    deezer_pic23 = deezer.find_one({"logo-22": {"$exists": "true"}})['logo-22']
    deezer_pic24 = deezer.find_one({"logo-23": {"$exists": "true"}})['logo-23']
    deezer_pic25 = deezer.find_one({"logo-24": {"$exists": "true"}})['logo-24']
    deezer_pic26 = deezer.find_one({"logo-25": {"$exists": "true"}})['logo-25']
    deezer_pic27 = deezer.find_one({"logo-26": {"$exists": "true"}})['logo-26']
    deezer_pic28 = deezer.find_one({"logo-27": {"$exists": "true"}})['logo-27']
    deezer_pic29 = deezer.find_one({"logo-28": {"$exists": "true"}})['logo-28']
    deezer_pic30 = deezer.find_one({"logo-29": {"$exists": "true"}})['logo-29']
    deezer_pic31 = deezer.find_one({"logo-30": {"$exists": "true"}})['logo-30']
    deezer_pic32 = deezer.find_one({"logo-31": {"$exists": "true"}})['logo-31']
    deezer_pic33 = deezer.find_one({"logo-32": {"$exists": "true"}})['logo-32']
    deezer_pic34 = deezer.find_one({"logo-33": {"$exists": "true"}})['logo-33']
    deezer_pic35 = deezer.find_one({"logo-34": {"$exists": "true"}})['logo-34']
    deezer_pic36 = deezer.find_one({"logo-35": {"$exists": "true"}})['logo-35']
    deezer_pic37 = deezer.find_one({"logo-36": {"$exists": "true"}})['logo-36']
    deezer_pic38 = deezer.find_one({"logo-37": {"$exists": "true"}})['logo-37']
    deezer_pic39 = deezer.find_one({"logo-38": {"$exists": "true"}})['logo-38']
    deezer_pic40 = deezer.find_one({"logo-39": {"$exists": "true"}})['logo-39']
    deezer_pic41 = deezer.find_one({"logo-40": {"$exists": "true"}})['logo-40']
    deezer_pic42 = deezer.find_one({"logo-41": {"$exists": "true"}})['logo-41']
    deezer_pic43 = deezer.find_one({"logo-42": {"$exists": "true"}})['logo-42']
    deezer_pic44 = deezer.find_one({"logo-43": {"$exists": "true"}})['logo-43']
    deezer_pic45 = deezer.find_one({"logo-44": {"$exists": "true"}})['logo-44']
    deezer_pic46 = deezer.find_one({"logo-45": {"$exists": "true"}})['logo-45']
    deezer_pic47 = deezer.find_one({"logo-46": {"$exists": "true"}})['logo-46']
    deezer_pic48 = deezer.find_one({"logo-47": {"$exists": "true"}})['logo-47']
    deezer_pic49 = deezer.find_one({"logo-48": {"$exists": "true"}})['logo-48']
    deezer_pic50 = deezer.find_one({"logo-49": {"$exists": "true"}})['logo-49']

    deezer_link1 = deezer.find_one({"link-0": {"$exists": "true"}})['link-0']
    deezer_link2 = deezer.find_one({"link-1": {"$exists": "true"}})['link-1']
    deezer_link3 = deezer.find_one({"link-2": {"$exists": "true"}})['link-2']
    deezer_link4 = deezer.find_one({"link-3": {"$exists": "true"}})['link-3']
    deezer_link5 = deezer.find_one({"link-4": {"$exists": "true"}})['link-4']
    deezer_link6 = deezer.find_one({"link-5": {"$exists": "true"}})['link-5']
    deezer_link7 = deezer.find_one({"link-6": {"$exists": "true"}})['link-6']
    deezer_link8 = deezer.find_one({"link-7": {"$exists": "true"}})['link-7']
    deezer_link9 = deezer.find_one({"link-8": {"$exists": "true"}})['link-8']
    deezer_link10 = deezer.find_one({"link-9": {"$exists": "true"}})['link-9']
    deezer_link11 = deezer.find_one({"link-10": {"$exists": "true"}})['link-10']
    deezer_link12 = deezer.find_one({"link-11": {"$exists": "true"}})['link-11']
    deezer_link13 = deezer.find_one({"link-12": {"$exists": "true"}})['link-12']
    deezer_link14 = deezer.find_one({"link-13": {"$exists": "true"}})['link-13']
    deezer_link15 = deezer.find_one({"link-14": {"$exists": "true"}})['link-14']
    deezer_link16 = deezer.find_one({"link-15": {"$exists": "true"}})['link-15']
    deezer_link17 = deezer.find_one({"link-16": {"$exists": "true"}})['link-16']
    deezer_link18 = deezer.find_one({"link-17": {"$exists": "true"}})['link-17']
    deezer_link19 = deezer.find_one({"link-18": {"$exists": "true"}})['link-18']
    deezer_link20 = deezer.find_one({"link-19": {"$exists": "true"}})['link-19']
    deezer_link21 = deezer.find_one({"link-20": {"$exists": "true"}})['link-20']
    deezer_link22 = deezer.find_one({"link-21": {"$exists": "true"}})['link-21']
    deezer_link23 = deezer.find_one({"link-22": {"$exists": "true"}})['link-22']
    deezer_link24 = deezer.find_one({"link-23": {"$exists": "true"}})['link-23']
    deezer_link25 = deezer.find_one({"link-24": {"$exists": "true"}})['link-24']
    deezer_link26 = deezer.find_one({"link-25": {"$exists": "true"}})['link-25']
    deezer_link27 = deezer.find_one({"link-26": {"$exists": "true"}})['link-26']
    deezer_link28 = deezer.find_one({"link-27": {"$exists": "true"}})['link-27']
    deezer_link29 = deezer.find_one({"link-28": {"$exists": "true"}})['link-28']
    deezer_link30 = deezer.find_one({"link-29": {"$exists": "true"}})['link-29']
    deezer_link31 = deezer.find_one({"link-30": {"$exists": "true"}})['link-30']
    deezer_link32 = deezer.find_one({"link-31": {"$exists": "true"}})['link-31']
    deezer_link33 = deezer.find_one({"link-32": {"$exists": "true"}})['link-32']
    deezer_link34 = deezer.find_one({"link-33": {"$exists": "true"}})['link-33']
    deezer_link35 = deezer.find_one({"link-34": {"$exists": "true"}})['link-34']
    deezer_link36 = deezer.find_one({"link-35": {"$exists": "true"}})['link-35']
    deezer_link37 = deezer.find_one({"link-36": {"$exists": "true"}})['link-36']
    deezer_link38 = deezer.find_one({"link-37": {"$exists": "true"}})['link-37']
    deezer_link39 = deezer.find_one({"link-38": {"$exists": "true"}})['link-38']
    deezer_link40 = deezer.find_one({"link-39": {"$exists": "true"}})['link-39']
    deezer_link41 = deezer.find_one({"link-40": {"$exists": "true"}})['link-40']
    deezer_link42 = deezer.find_one({"link-41": {"$exists": "true"}})['link-41']
    deezer_link43 = deezer.find_one({"link-42": {"$exists": "true"}})['link-42']
    deezer_link44 = deezer.find_one({"link-43": {"$exists": "true"}})['link-43']
    deezer_link45 = deezer.find_one({"link-44": {"$exists": "true"}})['link-44']
    deezer_link46 = deezer.find_one({"link-45": {"$exists": "true"}})['link-45']
    deezer_link47 = deezer.find_one({"link-46": {"$exists": "true"}})['link-46']
    deezer_link48 = deezer.find_one({"link-47": {"$exists": "true"}})['link-47']
    deezer_link49 = deezer.find_one({"link-48": {"$exists": "true"}})['link-48']
    deezer_link50 = deezer.find_one({"link-49": {"$exists": "true"}})['link-49']

    return render_template('index.html', logo=logo, spotify1=spotify1, spotify2=spotify2, spotify3=spotify3, spotify4=spotify4,
                           spotify5=spotify5, spotify6=spotify6, spotify7=spotify7, spotify8=spotify8,
                           spotify9=spotify9, spotify10=spotify10, spotify11=spotify11, spotify12=spotify12,
                           spotify13=spotify13, spotify14=spotify14, spotify15=spotify15, spotify16=spotify16,
                           spotify17=spotify17, spotify18=spotify18, spotify19=spotify19, spotify20=spotify20,
                           spotify21=spotify21, spotify22=spotify22, spotify23=spotify23, spotify24=spotify24,
                           spotify25=spotify25, spotify26=spotify26, spotify27=spotify27, spotify28=spotify28,
                           spotify29=spotify29, spotify30=spotify30, spotify31=spotify31, spotify32=spotify32,
                           spotify33=spotify33, spotify34=spotify34, spotify35=spotify35, spotify36=spotify36,
                           spotify37=spotify37, spotify38=spotify38, spotify39=spotify39, spotify40=spotify40,
                           spotify41=spotify41, spotify42=spotify42, spotify43=spotify43, spotify44=spotify44,
                           spotify45=spotify45, spotify46=spotify46, spotify47=spotify47, spotify48=spotify48,
                           spotify49=spotify49, spotify50=spotify50, spotify_pic1=spotify_pic1,
                           spotify_pic2=spotify_pic2, spotify_pic3=spotify_pic3, spotify_pic4=spotify_pic4,
                           spotify_pic5=spotify_pic5, spotify_pic6=spotify_pic6, spotify_pic7=spotify_pic7,
                           spotify_pic8=spotify_pic8, spotify_pic9=spotify_pic9, spotify_pic10=spotify_pic10,
                           spotify_pic11=spotify_pic11, spotify_pic12=spotify_pic12,spotify_pic13=spotify_pic13,
                           spotify_pic14=spotify_pic14, spotify_pic15=spotify_pic15, spotify_pic16=spotify_pic16,
                           spotify_pic17=spotify_pic17, spotify_pic18=spotify_pic18, spotify_pic19=spotify_pic19,
                           spotify_pic20=spotify_pic20, spotify_pic21=spotify_pic21, spotify_pic22=spotify_pic22,
                           spotify_pic23=spotify_pic23, spotify_pic24=spotify_pic24, spotify_pic25=spotify_pic25,
                           spotify_pic26=spotify_pic26, spotify_pic27=spotify_pic27, spotify_pic28=spotify_pic28,
                           spotify_pic29=spotify_pic29, spotify_pic30=spotify_pic30, spotify_pic31=spotify_pic31,
                           spotify_pic32=spotify_pic32, spotify_pic33=spotify_pic33, spotify_pic34=spotify_pic34,
                           spotify_pic35=spotify_pic35, spotify_pic36=spotify_pic36, spotify_pic37=spotify_pic37,
                           spotify_pic38=spotify_pic38, spotify_pic39=spotify_pic39, spotify_pic40=spotify_pic40,
                           spotify_pic41=spotify_pic41, spotify_pic42=spotify_pic42, spotify_pic43=spotify_pic43,
                           spotify_pic44=spotify_pic44, spotify_pic45=spotify_pic45, spotify_pic46=spotify_pic46,
                           spotify_pic47=spotify_pic47, spotify_pic48=spotify_pic48, spotify_pic49=spotify_pic49,
                           spotify_pic50=spotify_pic50, spotify_sing1=spotify_sing1,spotify_sing2=spotify_sing2,
                           spotify_sing3=spotify_sing3, spotify_sing4=spotify_sing4,spotify_sing5=spotify_sing5,
                           spotify_sing6=spotify_sing6, spotify_sing7=spotify_sing7,spotify_sing8=spotify_sing8,
                           spotify_sing9=spotify_sing9, spotify_sing10=spotify_sing10,spotify_sing11=spotify_sing11,
                           spotify_sing12=spotify_sing12,spotify_sing13=spotify_sing13,spotify_sing14=spotify_sing14,
                           spotify_sing15=spotify_sing15, spotify_sing16=spotify_sing16,spotify_sing17=spotify_sing17,
                           spotify_sing18=spotify_sing18, spotify_sing19=spotify_sing19,spotify_sing20=spotify_sing20,
                           spotify_sing21=spotify_sing21, spotify_sing22=spotify_sing22,spotify_sing23=spotify_sing23,
                           spotify_sing24=spotify_sing24, spotify_sing25=spotify_sing25,spotify_sing26=spotify_sing26,
                           spotify_sing27=spotify_sing27, spotify_sing28=spotify_sing28,spotify_sing29=spotify_sing29,
                           spotify_sing30=spotify_sing30, spotify_sing31=spotify_sing31,spotify_sing32=spotify_sing32,
                           spotify_sing33=spotify_sing33, spotify_sing34=spotify_sing34,spotify_sing35=spotify_sing35,
                           spotify_sing36=spotify_sing36, spotify_sing37=spotify_sing37,spotify_sing38=spotify_sing38,
                           spotify_sing39=spotify_sing39, spotify_sing40=spotify_sing40,spotify_sing41=spotify_sing41,
                           spotify_sing42=spotify_sing42, spotify_sing43=spotify_sing43,spotify_sing44=spotify_sing44,
                           spotify_sing45=spotify_sing45, spotify_sing46=spotify_sing46,spotify_sing47=spotify_sing47,
                           spotify_sing48=spotify_sing48, spotify_sing49=spotify_sing49, spotify_sing50=spotify_sing50,


                           youtube1=youtube1, youtube2=youtube2, youtube3=youtube3,
                           youtube4=youtube4, youtube5=youtube5, youtube6=youtube6, youtube7=youtube7,
                           youtube8=youtube8, youtube9=youtube9, youtube10=youtube10, youtube11=youtube11,
                           youtube12=youtube12, youtube13=youtube13, youtube14=youtube14, youtube15=youtube15,
                           youtube16=youtube16, youtube17=youtube17, youtube18=youtube18, youtube19=youtube19,
                           youtube20=youtube20, youtube21=youtube21, youtube22=youtube22, youtube23=youtube23,
                           youtube24=youtube24, youtube25=youtube25, youtube26=youtube26, youtube27=youtube27,
                           youtube28=youtube28, youtube29=youtube29, youtube30=youtube30, youtube31=youtube31,
                           youtube32=youtube32, youtube33=youtube33, youtube34=youtube34, youtube35=youtube35,
                           youtube36=youtube36, youtube37=youtube37, youtube38=youtube38, youtube39=youtube39,
                            youtube40=youtube40, youtube_pic1=youtube_pic1,
                           youtube_pic2=youtube_pic2, youtube_pic3=youtube_pic3, youtube_pic4=youtube_pic4,
                           youtube_pic5=youtube_pic5, youtube_pic6=youtube_pic6, youtube_pic7=youtube_pic7,
                           youtube_pic8=youtube_pic8, youtube_pic9=youtube_pic9, youtube_pic10=youtube_pic10,
                           youtube_pic11=youtube_pic11, youtube_pic12=youtube_pic12,youtube_pic13=youtube_pic13,
                           youtube_pic14=youtube_pic14, youtube_pic15=youtube_pic15, youtube_pic16=youtube_pic16,
                           youtube_pic17=youtube_pic17, youtube_pic18=youtube_pic18, youtube_pic19=youtube_pic19,
                           youtube_pic20=youtube_pic20, youtube_pic21=youtube_pic21, youtube_pic22=youtube_pic22,
                           youtube_pic23=youtube_pic23, youtube_pic24=youtube_pic24, youtube_pic25=youtube_pic25,
                           youtube_pic26=youtube_pic26, youtube_pic27=youtube_pic27, youtube_pic28=youtube_pic28,
                           youtube_pic29=youtube_pic29, youtube_pic30=youtube_pic30, youtube_pic31=youtube_pic31,
                           youtube_pic32=youtube_pic32, youtube_pic33=youtube_pic33, youtube_pic34=youtube_pic34,
                           youtube_pic35=youtube_pic35, youtube_pic36=youtube_pic36, youtube_pic37=youtube_pic37,
                           youtube_pic38=youtube_pic38, youtube_pic39=youtube_pic39, youtube_pic40=youtube_pic40,
                           youtube_link1=youtube_link1,
                           youtube_link2=youtube_link2, youtube_link3=youtube_link3, youtube_link4=youtube_link4,
                           youtube_link5=youtube_link5, youtube_link6=youtube_link6, youtube_link7=youtube_link7,
                           youtube_link8=youtube_link8, youtube_link9=youtube_link9, youtube_link10=youtube_link10,
                           youtube_link11=youtube_link11, youtube_link12=youtube_link12, youtube_link13=youtube_link13,
                           youtube_link14=youtube_link14, youtube_link15=youtube_link15, youtube_link16=youtube_link16,
                           youtube_link17=youtube_link17, youtube_link18=youtube_link18, youtube_link19=youtube_link19,
                           youtube_link20=youtube_link20, youtube_link21=youtube_link21, youtube_link22=youtube_link22,
                           youtube_link23=youtube_link23, youtube_link24=youtube_link24, youtube_link25=youtube_link25,
                           youtube_link26=youtube_link26, youtube_link27=youtube_link27, youtube_link28=youtube_link28,
                           youtube_link29=youtube_link29, youtube_link30=youtube_link30, youtube_link31=youtube_link31,
                           youtube_link32=youtube_link32, youtube_link33=youtube_link33, youtube_link34=youtube_link34,
                           youtube_link35=youtube_link35, youtube_link36=youtube_link36, youtube_link37=youtube_link37,
                           youtube_link38=youtube_link38, youtube_link39=youtube_link39, youtube_link40=youtube_link40,

                           yandex1 = yandex1, yandex2 = yandex2, yandex3 = yandex3, yandex4 = yandex4,
                           yandex5 = yandex5, yandex6 = yandex6, yandex7 = yandex7, yandex8 = yandex8,
                           yandex9 = yandex9, yandex10 = yandex10, yandex11 = yandex11, yandex12 = yandex12,
                           yandex13 = yandex13, yandex14 = yandex14, yandex15 = yandex15, yandex16 = yandex16,
                           yandex17 = yandex17, yandex18 = yandex18, yandex19 = yandex19, yandex20 = yandex20,
                           yandex21 = yandex21, yandex22 = yandex22, yandex23 = yandex23, yandex24 = yandex24,
                           yandex25 = yandex25, yandex26 = yandex26, yandex27 = yandex27, yandex28 = yandex28,
                           yandex29 = yandex29, yandex30 = yandex30, yandex31 = yandex31, yandex32 = yandex32,
                           yandex33 = yandex33, yandex34 = yandex34, yandex35 = yandex35, yandex36 = yandex36,
                           yandex37 = yandex37, yandex38 = yandex38, yandex39 = yandex39, yandex40 = yandex40,
                           yandex41 = yandex41, yandex42 = yandex42, yandex43 = yandex43, yandex44 = yandex44,
                           yandex45 = yandex45, yandex46 = yandex46, yandex47 = yandex47, yandex48 = yandex48,
                           yandex49 = yandex49, yandex50 = yandex50, deezer1=deezer1, deezer2=deezer2, deezer3=deezer3,
                           deezer4=deezer4,
                           deezer5=deezer5, deezer6=deezer6, deezer7=deezer7, deezer8=deezer8,
                           deezer9=deezer9, deezer10=deezer10, deezer11=deezer11, deezer12=deezer12,
                           deezer13=deezer13, deezer14=deezer14, deezer15=deezer15, deezer16=deezer16,
                           deezer17=deezer17, deezer18=deezer18, deezer19=deezer19, deezer20=deezer20,
                           deezer21=deezer21, deezer22=deezer22, deezer23=deezer23, deezer24=deezer24,
                           deezer25=deezer25, deezer26=deezer26, deezer27=deezer27, deezer28=deezer28,
                           deezer29=deezer29, deezer30=deezer30, deezer31=deezer31, deezer32=deezer32,
                           deezer33=deezer33, deezer34=deezer34, deezer35=deezer35, deezer36=deezer36,
                           deezer37=deezer37, deezer38=deezer38, deezer39=deezer39, deezer40=deezer40,
                           deezer41=deezer41, deezer42=deezer42, deezer43=deezer43, deezer44=deezer44,
                           deezer45=deezer45, deezer46=deezer46, deezer47=deezer47, deezer48=deezer48,
                           deezer49=deezer49, deezer50=deezer50, deezer_pic1=deezer_pic1,
                           deezer_pic2=deezer_pic2, deezer_pic3=deezer_pic3, deezer_pic4=deezer_pic4,
                           deezer_pic5=deezer_pic5, deezer_pic6=deezer_pic6, deezer_pic7=deezer_pic7,
                           deezer_pic8=deezer_pic8, deezer_pic9=deezer_pic9, deezer_pic10=deezer_pic10,
                           deezer_pic11=deezer_pic11, deezer_pic12=deezer_pic12,deezer_pic13=deezer_pic13,
                           deezer_pic14=deezer_pic14, deezer_pic15=deezer_pic15, deezer_pic16=deezer_pic16,
                           deezer_pic17=deezer_pic17, deezer_pic18=deezer_pic18, deezer_pic19=deezer_pic19,
                           deezer_pic20=deezer_pic20, deezer_pic21=deezer_pic21, deezer_pic22=deezer_pic22,
                           deezer_pic23=deezer_pic23, deezer_pic24=deezer_pic24, deezer_pic25=deezer_pic25,
                           deezer_pic26=deezer_pic26, deezer_pic27=deezer_pic27, deezer_pic28=deezer_pic28,
                           deezer_pic29=deezer_pic29, deezer_pic30=deezer_pic30, deezer_pic31=deezer_pic31,
                           deezer_pic32=deezer_pic32, deezer_pic33=deezer_pic33, deezer_pic34=deezer_pic34,
                           deezer_pic35=deezer_pic35, deezer_pic36=deezer_pic36, deezer_pic37=deezer_pic37,
                           deezer_pic38=deezer_pic38, deezer_pic39=deezer_pic39, deezer_pic40=deezer_pic40,
                           deezer_pic41=deezer_pic41, deezer_pic42=deezer_pic42, deezer_pic43=deezer_pic43,
                           deezer_pic44=deezer_pic44, deezer_pic45=deezer_pic45, deezer_pic46=deezer_pic46,
                           deezer_pic47=deezer_pic47, deezer_pic48=deezer_pic48, deezer_pic49=deezer_pic49,
                           deezer_pic50=deezer_pic50, deezer_sing1=deezer_sing1,deezer_sing2=deezer_sing2,
                           deezer_sing3=deezer_sing3, deezer_sing4=deezer_sing4,deezer_sing5=deezer_sing5,
                           deezer_sing6=deezer_sing6, deezer_sing7=deezer_sing7,deezer_sing8=deezer_sing8,
                           deezer_sing9=deezer_sing9, deezer_sing10=deezer_sing10,deezer_sing11=deezer_sing11,
                           deezer_sing12=deezer_sing12,deezer_sing13=deezer_sing13,deezer_sing14=deezer_sing14,
                           deezer_sing15=deezer_sing15, deezer_sing16=deezer_sing16,deezer_sing17=deezer_sing17,
                           deezer_sing18=deezer_sing18, deezer_sing19=deezer_sing19,deezer_sing20=deezer_sing20,
                           deezer_sing21=deezer_sing21, deezer_sing22=deezer_sing22,deezer_sing23=deezer_sing23,
                           deezer_sing24=deezer_sing24, deezer_sing25=deezer_sing25,deezer_sing26=deezer_sing26,
                           deezer_sing27=deezer_sing27, deezer_sing28=deezer_sing28,deezer_sing29=deezer_sing29,
                           deezer_sing30=deezer_sing30, deezer_sing31=deezer_sing31,deezer_sing32=deezer_sing32,
                           deezer_sing33=deezer_sing33, deezer_sing34=deezer_sing34,deezer_sing35=deezer_sing35,
                           deezer_sing36=deezer_sing36, deezer_sing37=deezer_sing37,deezer_sing38=deezer_sing38,
                           deezer_sing39=deezer_sing39, deezer_sing40=deezer_sing40,deezer_sing41=deezer_sing41,
                           deezer_sing42=deezer_sing42, deezer_sing43=deezer_sing43,deezer_sing44=deezer_sing44,
                           deezer_sing45=deezer_sing45, deezer_sing46=deezer_sing46,deezer_sing47=deezer_sing47,
                           deezer_sing48=deezer_sing48, deezer_sing49=deezer_sing49, deezer_sing50=deezer_sing50
                           ,deezer_link1=deezer_link1, deezer_link2=deezer_link2,
                           deezer_link3=deezer_link3, deezer_link4=deezer_link4, deezer_link5=deezer_link5,
                           deezer_link6=deezer_link6, deezer_link7=deezer_link7, deezer_link8=deezer_link8,
                           deezer_link9=deezer_link9, deezer_link10=deezer_link10, deezer_link11=deezer_link11,
                           deezer_link12=deezer_link12, deezer_link13=deezer_link13, deezer_link14=deezer_link14,
                           deezer_link15=deezer_link15, deezer_link16=deezer_link16, deezer_link17=deezer_link17,
                           deezer_link18=deezer_link18, deezer_link19=deezer_link19, deezer_link20=deezer_link20,
                           deezer_link21=deezer_link21, deezer_link22=deezer_link22, deezer_link23=deezer_link23,
                           deezer_link24=deezer_link24, deezer_link25=deezer_link25, deezer_link26=deezer_link26,
                           deezer_link27=deezer_link27, deezer_link28=deezer_link28, deezer_link29=deezer_link29,
                           deezer_link30=deezer_link30, deezer_link31=deezer_link31, deezer_link32=deezer_link32,
                           deezer_link33=deezer_link33, deezer_link34=deezer_link34, deezer_link35=deezer_link35,
                           deezer_link36=deezer_link36, deezer_link37=deezer_link37, deezer_link38=deezer_link38,
                           deezer_link39=deezer_link39, deezer_link40=deezer_link40, deezer_link41=deezer_link41,
                           deezer_link42=deezer_link42, deezer_link43=deezer_link43, deezer_link44=deezer_link44,
                           deezer_link45=deezer_link45, deezer_link46=deezer_link46, deezer_link47=deezer_link47,
                           deezer_link48=deezer_link48, deezer_link49=deezer_link49, deezer_link50=deezer_link50)



@app.route('/filter')
def filter():
    return render_template('filter.html')

if __name__ == "__main__":
    app.run(debug=True) #потом поставить False
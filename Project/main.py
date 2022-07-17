from flask import Flask, render_template
import pymongo
import os
mongo = pymongo.MongoClient()
mydb = mongo["charts"]

spotify = mydb["spotify"]
spotify_pic_db = mongo["pictures"]
spoti_pic_col = spotify_pic_db['spotify']

yandex = mydb["yandex"]
app = Flask(__name__)

@app.route('/')
def index():
    logo = os.path.join(r'D:\pythonProject\Charts\Project\static\images\logo.png')

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
                           spotify_pic50=spotify_pic50,

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
                           yandex49 = yandex49, yandex50 = yandex50)


@app.route('/filter')
def filter():
    return render_template('filter.html')

if __name__ == "__main__":
    app.run(debug=True) #потом поставить False
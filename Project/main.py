from flask import Flask, render_template
from Sources.yandex.yandex import collect_yandex_charts
from Sources.spotify.spotify import collect_spotify_charts
import json
app = Flask(__name__)
@app.route('/')
def index():
    with open(r"D:\pythonProject\Charts\Project\Sources\spotify\spotify_data.json") as json_file:
        data = json.load(json_file)
    return render_template('index.html', data=data)


@app.route('/filter')
def filter():
    return render_template('filter.html')

if __name__ == "__main__":
    app.run(debug=True) #потом поставить False
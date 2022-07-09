from flask import Flask, render_template
from Sources.yandex.yandex import collect_yandex_charts
from Sources.spotify.spotify import collect_spotify_charts
app = Flask(__name__)
# collect_yandex_charts()
# collect_spotify_charts()
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/filter')
def filter():
    return render_template('filter.html')

if __name__ == "__main__":
    app.run(debug=True) #потом поставить False
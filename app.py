from flask import Flask, render_template
from flask_navigation import Navigation


app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('início', 'index'),
    nav.Item('o que é voronoi?', 'voronoi'),
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/navpage')
def navpage():
    return render_template('navpage.html')

@app.route('/voronoi')
def voronoi():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
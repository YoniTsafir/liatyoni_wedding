# -*- coding=utf-8 -*-
import os

from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    return rsvp()

@app.route('/rsvp')
def rsvp():
    return render_template("rsvp.html")

@app.route('/pics')
def pics():
    return render_template("pics.html")

@app.route('/map')
def map():
    return render_template("map.html")

@app.route('/fbevent')
def fbevent():
    return render_template("fbevent.html")

@app.route('/tremps')
def tremps():
    return render_template("tremps.html")

@app.route('/calendar')
def calendar():
    return render_template("calendar.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


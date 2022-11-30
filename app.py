import flask
from flask import request, url_for, render_template, redirect


app = flask.Flask(__name__)

mapbox_access_token="pk.eyJ1Ijoib21lcnNhbGVlbTA5IiwiYSI6ImNsYjNxMjhycTAwczEzeG9hYmprbjU4d3IifQ.RfTRwUxxxUKV4K5uWq3pRQ"

@app.route('/',methods=['GET','POST'])
def index():
    return flask.render_template('index.html')


@app.route('/map',methods=['GET','POST'])
def mapview():
    return render_template('mapbox.html',
    mapbox_access_token=mapbox_access_token)


@app.route('/geo',methods=['GET','POST'])
def geoencode():
    return render_template('geocoding.html',
    mapbox_access_token=mapbox_access_token)

if __name__ == '__main__':
    app.run(debug=True)
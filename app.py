import flask
from flask import request, url_for, render_template, redirect


app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
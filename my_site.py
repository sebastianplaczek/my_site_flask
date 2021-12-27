from flask import Flask,render_template

app = Flask(__name__)

import os

PEOPLE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/')
def main_page():
    return render_template('index.html')
# @app.route('/starter')
# def starter():
#     return render_template('starter .html')



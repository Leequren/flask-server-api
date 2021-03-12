from flask import Flask, render_template, request, redirect, jsonify
from flask_wtf import FlaskForm
import flask
import api
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def login():
    print(requests.get('http://7c904182afa7.ngrok.io/api/2466083888').json())



if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.register_blueprint(api.blueprint)
    app.run(host='127.0.0.1', port=8080)

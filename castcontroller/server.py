"""
Web API for CastController.
"""

import time

from flask import Flask, request
from flask_cors import CORS

from castcontroller import main

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "CastController is up!"


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/play', methods=['POST'])
def play():
    main.play()
    return {'result': True}


@app.route('/pause', methods=['POST'])
def pause():
    main.pause()
    return {'result': True}


@app.route('/toggle', methods=['POST'])
def toggle():
    main.toggle()
    return {'result': True}


@app.route('/start', methods=['POST'])
def start():
    body = request.json
    url = body.get("url")
    content_type = body.get("content_type")
    main.start(url, content_type)
    return {'result': True}


@app.route('/stop', methods=['POST'])
def stop():
    main.stop()
    return {'result': True}


@app.route('/seek', methods=['POST'])
def seek():
    body = request.json
    abs = body.get("abs", None)
    rel = body.get("rel", None)
    main.seek(abs=abs, rel=rel)
    return {'result': True}


@app.route('/volume', methods=['POST'])
def volume():
    body = request.json
    rel = body.get("rel")
    main.volume(rel)
    return {'result': True}


@app.route('/status', methods=['GET'])
def duration():
    status = main.status()
    return {'result': status}

# -*- coding: utf-8 -*-

"""
    VR Theater Server Control
    ~~~~~~~~~~~~~~~~~~~~~~~
    Administration tool for the VR Theater Game Server
    :copyright: (c) 2021 by Daniel Stock.
"""

import os
from sys import platform
from time import sleep
from datetime import datetime
from subprocess import check_output, check_call
from flask import Flask, render_template, jsonify


# ------------------------------------------------------------------------------
# INIT
# ------------------------------------------------------------------------------

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
os.environ['FLASK_ENV'] = app.config['ENVIRONMENT']

# ------------------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------------------


@app.route('/')
def index():
    return render_template('index.html', environment=os.environ['FLASK_ENV'])


@app.route('/log')
def log():
    def generate():
        if platform == "linux" or platform == "linux2":
            logfile = "/var/log/vollstock/game-server.log"
        elif platform == "darwin":
            # logfile = "/Users/vollstock/Library/Logs/Unity/Editor.log"
            logfile = "/var/log/system.log"

        with open(logfile) as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype='text/plain')


@app.route('/status')
def status():
    try:
        if platform == "linux" or platform == "linux2":
            # Active: active (running) since Tue 2021-05-25 15:35:42 CEST; 22h
            result = os.popen(
                'systemctl status vr-theater-server | grep Active').readline()
        elif platform == "darwin":
            # dummy implementation for dev
            odd = (datetime.now().second % 10) > 3
            if odd:
                result = "Active: active (running) since Tue 2021-05-25 15:35:42 CEST; 22h"
            else:
                result = "Active: inactive (dead) since Wed 2021-05-26 14:33:15 CEST; 1s"
    except Exception as e:
        raise e

    status = dict()
    status['isRunning'] = True if result.rstrip(
        '\n').split()[1] == "active" else False
    return jsonify(status)


@app.route('/start')
def start():
    try:
        if platform == "linux" or platform == "linux2":
            check_call(["systemctl", "start", "vr-theater-server"])
    except Exception as e:
        return jsonify(False)
    return jsonify(True)


@app.route('/stop')
def stop():
    try:
        if platform == "linux" or platform == "linux2":
            check_call(["systemctl", "stop", "vr-theater-server"])
    except Exception as e:
        return jsonify(False)
    return jsonify(True)


@app.route('/restart')
def restart():
    try:
        if platform == "linux" or platform == "linux2":
            check_call(["systemctl", "restart", "vr-theater-server"])
    except Exception as e:
        return jsonify(False)
    return jsonify(True)


# ------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT']
    )

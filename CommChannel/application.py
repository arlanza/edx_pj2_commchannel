import os
import requests

from flask import Flask, jsonify, render_template, request, session
from flask_socketio import SocketIO, emit
from classes.message import *
from datetime import datetime
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)





# List of channels  [channelname, [message1,...,messageN]]
channels = dict();

@app.route("/")
def index():

    # Using global channels
    global channels

    return render_template("index.html",channels=channels)

@app.route("/createchannel", methods=["POST"])
def createchannel():

    global channels

    # Get data form
    username = request.form.get("text-username")
    channelname = request.form.get("text-channelname")

    if channelname not in channels:
        channels[channelname] = None
        msgResult="New Channel "+ channelname + "added"
    else:
        msgResult="Channel "+ channelname + "previously added"

    return render_template("index.html",channels=channels, msgResult=msgResult)

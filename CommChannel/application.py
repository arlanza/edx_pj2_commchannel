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
        msgResult="New Channel "+ channelname + " added"
    else:
        msgResult="Channel "+ channelname + " previously added"

    return render_template("index.html",channels=channels, msgResult=msgResult)

@app.route("/channel/<string:channelname>", methods=["POST","GET"])
def channel(channelname):
    global channels

    msgResult=""
    return render_template("channel.html", channelname=channelname, messages=channels[channelname], msgResult=msgResult)

@app.route("/createmessage/<string:channelname>", methods=["POST"])
def createmessage(channelname):
    global channels
    username = request.form.get("text-username")
    textmessage = request.form.get("text-message")
    message = Message(username, datetime.now(), textmessage)


    messages=channels[channelname]
    if not channels[channelname]:
        channels[channelname]=[message]
    else:
        channels[channelname].append(message)

    msgResult=""
    return render_template("channel.html", channelname=channelname, messages=channels[channelname], msgResult=msgResult)

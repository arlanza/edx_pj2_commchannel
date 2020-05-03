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

    #message1 = Message("Laura1111",datetime.now(),"Mensaje11111")
    #message2 = Message("Laura1111",datetime.now(),"Mensaje22222")

    # channels["1"+username]=[message1,message2]
    #channels[username]=[message1,message2]
    #channels[channelname]=[message1,message2]
    channels[channelname] = None

    return render_template("index.html",channels=channels)

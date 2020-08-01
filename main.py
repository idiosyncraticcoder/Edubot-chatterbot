from coronabot import coronachatbot
from blmbot import blmchatbot
from yemenbot import yemenchatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/coronabot")
def getcoronabot():
    return render_template("coronabot.html")

@app.route("/blmbot")
def getblmbot():
    return render_template("blmbot.html")

@app.route("/yemenbot")
def getyemenbot():
    return render_template("yemenbot.html")

@app.route("/coronabot/get")
def get_coronabot_response():
    userText = request.args.get('msg')
    return str(coronachatbot.get_response(userText))

@app.route("/blmbot/get")
def get_blmbot_response():
    userText = request.args.get('msg')
    return str(blmchatbot.get_response(userText))

@app.route("/yemenbot/get")
def get_yemenbot_response():
    userText = request.args.get('msg')
    return str(yemenchatbot.get_response(userText))

if __name__ == "__main__":
    app.run()

from flask import Flask,render_template,request,redirect,jsonify,url_for
from song import WordFreq
from random import choice
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/", methods=["POST"])
def writeToFile():
    artistName = request.form['artistName']
    songName = request.form['songName']
    errorMsg="Couldn't find it in database, try again"
    try:
        lyric = WordFreq(artistName,songName)
        lyricData = lyric.cleanData()
        lyric.pushToDict(lyricData)
        lyric.writeToFile()
        return redirect(url_for('renderCharts'))
    except ValueError:
        return(redirect(url_for('home')))

@app.route("/chart",methods=["POST","GET"])
def renderCharts():
    filename = os.path.join("freqword.json")
    with open(filename) as file:
        data=json.load(file)
        listify=jsonify(data)
        arrWord=[]
        arrCount=[]
        colorCodes = []
        for key, value in data.items():
            arrWord.append(key)
            arrCount.append(value)
            colorCodes.append(colorGen())
        return render_template('charts.html',arrWord=arrWord,arrCount=arrCount,
                               colorCodes=colorCodes,
                               zipList=zip(arrWord,arrCount))

#generating random colors depending on how many words we have
def colorGen():
    hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','f']
    code='#'
    for i in range(0,6):
        code+=choice(hex_chars) #choice returns random combinations from hex
    return code

if __name__=="__main__":
    app.run(debug=True)

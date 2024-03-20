import random
from flask import Flask, render_template, request, redirect, url_for, session, send_file
#import tarih
# from getmac import get_mac_address as gma
from datetime import timedelta
#import ceviri
#import time
import requests
#import geocoder
import sqlite3
import os
import datetime



mytoken = "5697811443:AAF1qVasdxI1Z8vZ4FuHMapDO1yhHGAK7-A"
url = "https://api.telegram.org/bot" + mytoken + "/"
myTelegramId = 109409330


def sendmessage(text, telegramid=myTelegramId, url=url):
    msj = {"chat_id": telegramid, "text": text}
    result = requests.post(url + "sendMessage", json=msj)



app = Flask(__name__)
app.secret_key = "kelimix"


@app.before_request
def log_request():
    now = datetime.datetime.now()
    request_data = f"{now} - Request URL: {request.url} \\\\nRequest Method: {request.method} \\\\nRequest IP: {request.remote_addr} \\\\nRequest Headers: {request.headers} \\\\nRequest Body: {request.get_data()} \\\\n"
    with open("request_logs.txt", "a") as f:
        f.write(request_data)




@app.route('/')
def index():

    grup_liste=[]
    with sqlite3.connect("flemenkce_kelime_cumle.db") as vt:
        cursor = vt.cursor()        

    cursor.execute("SELECT grup, grup_2 FROM tablo_1")
    gruplar = cursor.fetchall()
    vt.commit()
    for i in gruplar:
        if ([i[0],i[1]] not in grup_liste) and ( len(str(i[0]))>5):
            grup_liste.append([i[0],i[1]])





    return render_template("index.html",grup_liste=grup_liste)




@app.route('/test.html')
def test_html():

    try:

        test_listesi = []
        with sqlite3.connect("flemenkce_kelime_cumle.db") as vt:
            cursor = vt.cursor()        

        cursor.execute("SELECT * FROM tablo_1 WHERE grup_2 = '{}'  ORDER BY random() LIMIT 1 ".format(session["test_grup"]))
        kelime = cursor.fetchall()
        print(kelime)
        vt.commit()
        session["kelime"]=kelime
        session["sesli_okuma_kelime"]=kelime[0][1]

     
        sendmessage("{}\n".format(
                kelime))

        return render_template("test.html")
    except:
        return redirect(url_for("index"))





@app.route('/test_sec', methods=["POST", "GET"])
def test_sec_db():
    if request.method == "POST":
        try:
            test_grup = request.form["test_grup"]
            session["test_grup"]=test_grup

            return redirect(url_for("test_html"))
        except:
            print(" hatalı")
            return redirect(url_for("index"))
        




@app.route('/sesli_okuma', methods=["POST", "GET"])
def sesli_okuma_db():
    import sesli_okuma
    if request.method == "POST" or "GET":
        try:
            x=sesli_okuma.speak(session["sesli_okuma_kelime"])
            print(x)
            return render_template("test.html")
        except:
            print(" hatalı")
            return render_template("test.html")






if __name__ == '__main__':
    app.debug = False
    app.run(host="0.0.0.0", port=5015)
    # app.run()

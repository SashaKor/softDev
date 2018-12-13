# Aleksandra Koroza
# Softdev1 pd8
# K#25: Getting More REST
#2018-14-11

from flask import Flask, render_template
import json
import urllib.request as request

app = Flask(__name__)

@app.route('/')
def home():
    #API_KEY not necessary for used API
    URL = 'http://skateipsum.com/get/3/1/JSON'
    response = request.urlopen(URL)
    response = response.read()
    info = json.loads(response)
    return render_template('index.html',api=info[1])

if __name__ == '__main__':
    app.debug=True
    app.run()

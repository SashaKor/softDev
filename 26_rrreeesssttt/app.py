# Aleksandra Koroza
# Softdev1 pd8
# K#26: Getting More REST
#2018-15-11

from flask import Flask, render_template
import json
import urllib.request as request

app = Flask(__name__)

@app.route('/')
def home():
    #jService API (damian W.)
    #API_KEY not necessary
    URL1 = 'http://jservice.io/api/random'
    jinfo= fetchInfo(URL1)
    jq= jinfo[0]['question']
    ja= jinfo[0]['answer']
    jc= jinfo[0]['airdate']

    #Advice Slip API (daniel G.)
    URL2 = 'https://api.adviceslip.com/advice'
    ainfo= fetchInfo(URL2)
    ad = ainfo['slip']['advice']

    #Climate Data API (fabiha T.)
    # year range, country, and desired data currently specified in link
    URL3 = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/bccr_bcm2_0/a2/tas/2020/2039/usa"
    cinfo= fetchInfo(URL3)
    tps = cinfo[0]['monthVals']

    return render_template('index.html',
    jquestion=jq,
    janswer=ja,
    jcreate=jc,
    advice= ad,
    temps = tps
    )

#returns loaded response
def fetchInfo(url):
    response = request.urlopen(url)
    response = response.read()
    info = json.loads(response)
    return info

if __name__ == '__main__':
    app.debug=True
    app.run()

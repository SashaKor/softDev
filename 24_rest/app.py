#Aleksandra Koroza
#SoftDev1 pd8
#24: A RESTful Journey Skyward
#2018-11-13

#https://api.nasa.gov/planetary/apod?api_key=QcFjChAvmC3e7EIA8nWtWpX7JzkYjK9vJIN6FZfE
# my personal api key for NASA
from flask import Flask, render_template

import urllib
app = Flask(__name__) #create instance of class Flask

#string of response recieved as a result of API query
fetchedData = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=QcFjChAvmC3e7EIA8nWtWpX7JzkYjK9vJIN6FZfE").read()
imgUrl = str(fetchedData).split('"url":')[1]

@app.route("/")
def space():
    url = imgUrl.replace("}","").replace("'", "").replace("\"", "").replace("\\n", "").strip()
    print("url: '" + url + "'")
    return render_template('text.html',link=str(url))

if __name__ == "__main__":
    app.debug = True
    app.run()

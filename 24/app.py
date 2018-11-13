#Aleksandra Koroza, Thomas Zhao
#SoftDev1 pd8
#K #10: Jinja Tuning
#2018-09-23
#https://api.nasa.gov/planetary/apod?api_key=QcFjChAvmC3e7EIA8nWtWpX7JzkYjK9vJIN6FZfE
# my personal api key for NASA
from flask import Flask,render_template
from util import occupations
app = Flask(__name__) #create instance of class Flask

#
dict = urllib.request(https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=QcFjChAvmC3e7EIA8nWtWpX7JzkYjK9vJIN6FZfE)
@app.route("/")
def space():
    print(dict)
    return render_template('text.html',p=image )


if __name__ == "__main__":
    app.debug = True
    app.run()

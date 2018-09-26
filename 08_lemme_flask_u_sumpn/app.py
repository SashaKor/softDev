#Aleksandra Koroza
#SoftDev pd8
#08_lemme_flask_u_sumpn
#2018-09-19

from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor

@app.route('/')
def home():
 return 'Atom is the best religion'

from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor

@app.route('/')
def home1():
 return '<a href= /hello> oh no </a>'

@app.route('/hello')
def home2():
 return '<a href= /hello/world> oh nah </a>'

@app.route('/hello/world')
def home3():
 return 'ya"ll'
  
app.debug = True
app.run()

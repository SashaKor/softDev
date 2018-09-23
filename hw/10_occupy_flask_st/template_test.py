from flask import Flask,render_template
app = Flask(__name__) #create instance of class Flask

coll = [0,1,1,2,3,5,8]

#@app.route("/")
#def being():
#    return "<a href='/static/text.html'> Go here </a>"

@app.route("/")
def hello_world(): #assign fxn to route
    return render_template(
        'text.html',
        foo = "fooo",
        c = coll
        )



app.debug = True

if __name__ == "__main__":
    app.debug = True
    app.run()

#Aleksandra Koroza
#SoftDev1 pd8
#13: Echo Echo Echo .
#2018-09-27  

from flask import Flask,render_template,request
app = Flask(__name__) #create instance of class Flask


@app.route("/",methods= ["GET","POST"])
def hello_world(): #assign fxn to route
    print(app)
    return render_template('input.html')

@app.route("/auth",methods= ["GET","POST"])
def authenticate() :
    print(app)
    print(request)
    print(request.args['username'])
    return render_template('output.html',
                           username=request.post('username')
                           method= request)
    
 
if __name__ == "__main__":
        app.debug = True
        app.run()


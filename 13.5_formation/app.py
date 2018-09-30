#Aleksandra Koroza
#SoftDev1 pd8
#13.5: Echo Echo Echo .
#2018-09-27  
# ctrl shift i --> go to network, headers to see what method is used (console)
from flask import Flask,render_template,request
app = Flask(__name__) #create instance of class Flask


@app.route("/",methods=["POST","GET"])
def hello_world(): #assign fxn to route
    print(app)
    return render_template('input.html')

@app.route("/auth",methods=["POST","GET"])
def authenticate():
    #print(app)
    print(request)
    #print(request.args['username'])
    if request.method == 'POST':
        user= request.form['username']
        return render_template('output.html',username=user,
                               method=request.method)
    else:
        user=request.args.get('username')
        return render_template('output.html',username=user,
                                       method=request.method)

 
if __name__ == "__main__":
    app.debug = True
    app.run()


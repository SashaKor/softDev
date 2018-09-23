# Korhao: Aleksandra K., Thomas Z.
#SoftDev1 pd8
#K #10: Jinja Tuning 
#2018-09-23 


from flask import Flask,render_template
import random
app = Flask(__name__) #create instance of class Flask

#coll = [0,1,1,2,3,5,8]
# picking an occupation code
def pickOccupation():
    file = open("occupations.csv",'r')
    info = file.read().split("\n")
    file.close()
    
    info.pop(0) # Title line
    info.pop(len(info)-1) # Last line
    info.pop(len(info)-1) # again due to some issue with csv
    
    #print('info length:')
    #print(len(info))
    
    # Initialize dictionary
    book = {}
    for x in range(0,len(info)):
        if info[x].count(',') == 1:
            line = info[x].split(",")
            book[line[0]] = float(line[1])
        else: 
            # more than 1 comma
            lastC = info[x].rindex(',')
            book[info[x][0:lastC]] = float(info[x][lastC+1:len(info[x])])

    target = random.uniform(0, 99.8)
    current = 0

    for entry in book:
        current = current + book[entry]
        if current > target:
            
            return entry,book
        

@app.route("/")
def hello_world(): #assign fxn to route
    f,b= pickOccupation()
    return render_template(
        'text.html',
        foo = f,
        c = b
        )


app.debug = True

if __name__ == "__main__":
    app.debug = True
    app.run()

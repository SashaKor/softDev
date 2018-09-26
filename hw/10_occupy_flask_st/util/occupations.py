import random
#the mechanism behind our random selection
# picking an occupation code

def readFile():
    file = open('data/occupations.csv','r')
    info = file.read().split("\n")
    file.close()
    
    info.pop(0) # Title line
    info.pop(len(info)-1) # Last line
    info.pop(len(info)-1) # again due to some issue with csv
    return info

def pickOccupation(): 
    # Initialize dictionary
    info= readFile()
    book = {}
    for entry in range(0,len(info)):
        if info[entry].count(',') == 2:
            line = info[entry].split(",")
            book[line[0]] = (float(line[1]), line[2])
        else: 
            # more than 2 commas
            storage = info[entry].split('"') #splits by "
            storage.remove('') #removes '' element
            resplit = storage[1].split(',') #splits num&link element by ,
            resplit.remove('') #removes '' elements
            storage.append(resplit)
            storage.pop(1) #removes useless element 
            #storage's format is [name, [number, link] ]

            book[storage[0]] = (float(storage[1][0]), storage[1][1])
            #book's format is {name: (number, link) ... }

    target = random.uniform(0, 99.8)
    current = 0
    
    for entry in book:
        current = current + book[entry][0]
        if current > target:
            return entry,book
        

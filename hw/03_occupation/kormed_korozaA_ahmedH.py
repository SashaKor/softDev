#Kormed: Aleksandra Koroza, Hasif Ahmed
#SoftDev1 pd8
#06: StI/O: Divine your Destiny!
#2018-09-13

#TASK 1: Write a Python script to read in the file and
#build an appropriate dictionary from it.
#Make sure the percentages are stored as numbers.

import csv

#source: https://realpython.com/python-csv/
#reads and returns a dictionary
def read(file):
    f = open(file) #stores file info in file object "f"
    open_f = csv.reader(f) #open_f is a csv.reader object
    dict= {}
    
    #for every line
    for row in open_f:
        try:
            dict[row[0]]=float(row[1])
        except:
            continue

    print(dict)
        
read('occupations.csv')

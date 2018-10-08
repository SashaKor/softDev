#Aleksandra Koroza, Vincent Chi: Chiroza
#SoftDev1 pd8
#K #17: Average  
#2018-10-07

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



DB_FILE="discobandit.db" #delete before every subsequent run

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# creates and populates table from csvfile with three specified columns
def createTable(filename,tblname,par1,par2,par3):
     with open(filename, newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          tblcommand = "CREATE TABLE {0}({1} TEXT, {2} INTEGER, {3} INTEGER)".format(tblname,par1,par2,par3)
          c.execute(tblcommand) #creates the table with specified parameters

          insertHdr = "INSERT INTO {0} ({1},{2},{3}) VALUES ".format(tblname,par1,par2,par3)
          for row in reader:
               insrtcommand = insertHdr + "('{0}','{1}','{2}')".format(row[par1],row[par2],row[par3])
               c.execute(insrtcommand)
               
#create tables for peeps.csv
createTable('peeps.csv',"peeps","name","age","id")
#create table for courses.csv
createTable('courses.csv',"courses","code","mark","id")




#==========================================================

db.commit() #save changes
db.close()  #close database

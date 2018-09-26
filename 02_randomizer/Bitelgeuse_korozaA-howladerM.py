#Team Bitelguese (Aleksandra Koroza and Mohtasim Howlader)
#SoftDev1 pd8
#K #02: NO-body expects the Spanish Inquisition!
#2018-09-12

#dictionary w/ list
#Your SOLO TASK: Use your Python knowledge and resourceful trickery to write a program that will print the name of a randomly-selected student from team (w, m, or x).

import random

KREWES = {
'w': ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],
'm': ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],
'x': ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']
}


def randPerson(letter):
    valList= KREWES[letter]  #first access the list of values
    
    #alternative way of dealing with duplicates (by making sure they don't exist in the first place)
    #valSet = set(valList) #convert list to set to eliminate duplicates
    #valList = list(valSet) #convert set back to list
    
    loc= random.randint(0,len(valList)-1)  #generate a random location
    print "Your selected person is "+ valList[loc]+ ", their index in the list being: "+ str(loc) +"."  #accessing name using loc as index, done to address above duplicate issue w/o deleting person.


randPerson('w')
randPerson('m')
randPerson('x')







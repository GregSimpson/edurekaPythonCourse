# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:18:23 2016

@author: greg.simpson
"""

from random import randint

numberCorrect =0
totalQuestions=0

def runMain(num1, num2, type, solved):
    # this is the main function

    validTypes = ['M','A','S','D']
    
    def sp_type():
        type = raw_input("Specify the question type(multiplication:M, addition:A, subtraction:S, division:D):")
        print "Please input only char  " + str(validTypes)
        return type 
        
    type = ""
    while type not in validTypes:
        if type not in validTypes:
            type = sp_type()

    if type == 'M':
        ans = input("What is %d times %d? " % (num1,num2))
        result = num1 * num2
            
    if type == 'A':
        ans = input("What is %d plus %d? " % (num1,num2))
        result = num1 + num2
        
    if type == 'S':
        ans = input("What is %d minus %d? " % (num1,num2))
        result = num1 - num2

    if type == 'D':
        ans = input("What is %d divided by %d? " % (num1,num2))
        result = num1 / num2

        
    if ans == result:
        print(" Correct - very good.\n")
        solved += 1
    else:
        print(" Incorrect - the answer is %d \n" % result)
        
    return solved


def start_puzzle(numberCorrect, totalQuestions): 
    level = ''
    play_level = ['easy', 'intermediate', 'hard']
    print(play_level)    
    
    while level not in play_level:
        level = raw_input("Which level you wanted to be in(easy, intermediate, hard): ")
        if level not in play_level:
            print "Please enter correct level name.."
            
    num_q = input('Enter the number of questions: ')
    try:
        if int(num_q):
            pass
    except ValueError:
        print "I am afraid %s is not a number" % num_q
        
    totalQuestions = num_q
    
    for number_q in range(1,num_q+1):
        if level == 'easy':
            num1 = randint(1,10)
            num2 = randint(1,10)
            numberCorrect = runMain(num1, num2, type, numberCorrect)
        if level == 'intermediate':
            num1 = randint(1,20)
            num2 = randint(1,20)
            numberCorrect = runMain(num1, num2, type, numberCorrect)
        if level == 'hard':
            num1 = randint(1,30)
            num2 = randint(1,30)
            numberCorrect = runMain(num1, num2, type, numberCorrect)
                        
    return(numberCorrect,totalQuestions)

startQuestion="want to start the puzzle(yes/no) ? :"
inp = raw_input(startQuestion)
#inp = "yes"
while inp != 'no':
    numberCorrect,totalQuestions = start_puzzle(numberCorrect,totalQuestions)
    inp = raw_input(startQuestion)
    
print "\nOut of %s questions asked. You got %d of them right." % (totalQuestions,numberCorrect)
print "Well done!\n\n"

print " PART 2 - recursive exponent"
def myExp(x,n):
    if n == 0:
        return 1
    elif (n % 2 == 0):
        return myExp(x*x, n/2)
    else:
        return x * myExp(x,n-1)

print ("2^^3 == " + str(myExp(2,3)))
print ("3^^2 == " + str(myExp(3,2)))

print " \n\nPART 3 - lambda function"
mylist = [["john", 1, "a"], ["larry", 0, "b"]]
mylist.sort(key=lambda x: x[0])
print(mylist)
mylist.sort(key=lambda x: x[1])
print(mylist)
mylist.sort(key=lambda x: x[2])
print(mylist)

print " \n\nPART 4 - itemgetter function"
from operator import itemgetter
mylist.sort(key=itemgetter(0))
print(mylist)
mylist.sort(key=itemgetter(1))
print(mylist)
mylist.sort(key=itemgetter(2))
print(mylist)


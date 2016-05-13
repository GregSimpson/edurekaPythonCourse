# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:19:18 2016

@author: greg.simpson
"""

# code warrior 1

#def double_char(s):
#    result = ''
#    for char in s:
#        result += char * 2
#    return result

print ("\nKata : double chars  ---------------- " )  
# Best answer
def double_char(s):
    return ''.join(c * 2 for c in s)
              
print (double_char("String"))
print (double_char("Hello World"))
print (double_char("1234!_ "))
print ("Kata : END ---------------- \n" )

#code warrior 2
print ("\nKata : sum range if 3 or 5 prime numbers  ---------------- " )  
def solution(maxRange):
    sum = 0
    for x in range(maxRange):
        #print x
        if (x%3 == 0 ) or (x%5 == 0):
            #print (x)
            sum += x
    return sum
    
# Best answer
# def solution(number):
#    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)    
        
print (solution(10))
print ("Kata : END ---------------- \n" )


print ("\nKata : function iterators ---------------- " )  

# http://d3l8wp33uu8nxs.cloudfront.net/kata/function-iteration/discuss/python
   
# the function createIterator returned another function, 
#  and that function would receive the input outside. 
# https://github.com/hbdhj/python/blob/master/codewars/43.py
# Function iteration
def create_iterator(func, num):
    # TODO: Write code here to return a function
    # that executes *func*, *n* times on a supplied input
    print ("create_iterator - func is : " + str(func) )
    print ("create_iterator - num  is : " + str(num) )

    def multiple_func(p):
        print ("multi_fct - p is : " + str(p) )
        ret = p
        n = num
        while n>0:
            ret=func(ret)
            n-=1
        return ret
    return multiple_func

print("Iterator for 'get_double' function")
def get_double(n):
    print ("get_double - n is : " + str(n) )
    return 2*n

print("Running the iterator once")
double_iterator = create_iterator(get_double, 1)

assert(double_iterator(3)==6)
#assert(double_iterator(5)==10)

#print("Running the iterator twice")
#get_quadruple = create_iterator(get_double, 2)

#assert(get_quadruple(2)==8)
#assert(get_quadruple(5)==20)

print (create_iterator(get_double, 2))

print (double_iterator(4))
  
print ("Kata : END ---------------- \n" )

print ("\nKata :  bracket matching ---------- " )

# A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.
# Your function will take an input string that may contain any of the symbols "()" "{}" or "[]" to create groups.
# It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.

# These are done correctly
# ({})
# [[]()]
# [{()}]
# The next are done incorrectly
# {(})
# ([]
# [])

    
def group_check(s):
    print("group_check received : " + s)
    openCounter = 0
    
    openChars=[ "(","{","[" ]
    closeChars=[ ")","}","]" ]
    listOfGroupers = [];    
    combos = {'(': ')', '{': '}', '[': ']'}

    for each_char in s:
        if each_char in openChars:
            #print "OPEN : " + str(each_char)
            openCounter += 1
            
            #listOfGroupers.append(each_char)
            listOfGroupers.append(combos[each_char])
            #print("added to list : " + str(combos[each_char]))
            #print("added char.  list now says : " + str(listOfGroupers))
        elif each_char in closeChars:   
            if ( not listOfGroupers ):
                #print("\tGJS EMPTY LIST")
                print("\tBAD SYNTAX - extra closing char unexpected : " + each_char)
                return False
            else:
                #print("\tGJS NOT empty list")
                #print "CLOSE : " + str(each_char)
                openCounter -= 1
                #print("last in list : " + str((listOfGroupers[-1])))
                #print (listOfGroupers[-1])

                if ( listOfGroupers[-1] <> each_char):
                    print("\tBAD SYNTAX - match expected : " + listOfGroupers[-1] + " found : " + each_char)
                    #listOfGroupers.remove(listOfGroupers[-1])
                    return False
                else:
                    #print(" FOUND expected char : " + listOfGroupers[-1])
                    listOfGroupers.pop(-1)
                    #print("removed it.  list now says : " + str(listOfGroupers))

    return (len(listOfGroupers) == 0 )

print( str(group_check("()")) + "\n" )
print( str(group_check("({")) + "\n" )
print( str(group_check("({[]})")) + "\n" )
print( str(group_check("(some)things in here")) + "\n" )
print( str(group_check("begin(middle{ending )")) + "\n" )
print( str(group_check("begin(middle{ending } } )")) + "\n" )
print( str(group_check("begin(middle{ending } ) )")) + "\n" )


def group_check_clean(s):
    print("group_check_clean received : " + s)
    openCounter = 0
    
    openChars=[ "(","{","[" ]
    closeChars=[ ")","}","]" ]
    listOfGroupers = [];    
    combos = {'(': ')', '{': '}', '[': ']'}

    for each_char in s:
        if each_char in openChars:
            openCounter += 1            
            listOfGroupers.append(combos[each_char])
        elif each_char in closeChars:   
            if ( not listOfGroupers ):
                print("\tBAD SYNTAX - extra closing char unexpected : " + each_char)
                return False
            else:
                openCounter -= 1
                if ( listOfGroupers[-1] <> each_char):
                    print("\tBAD SYNTAX - match expected : " + listOfGroupers[-1] + " found : " + each_char)
                    return False
                else:
                    listOfGroupers.pop(-1)

    return (len(listOfGroupers) == 0 )

print( str(group_check_clean("()")) + "\n" )
print( str(group_check_clean("({")) + "\n" )
print( str(group_check_clean("({[]})")) + "\n" )
print( str(group_check_clean("(some)things in here")) + "\n" )
print( str(group_check_clean("begin(middle{ending )")) + "\n" )
print( str(group_check_clean("begin(middle{ending } } )")) + "\n" )
print( str(group_check_clean("begin(middle{ending } ) )")) + "\n" )



# solution close to what I was aiming for
#  but it does not allow any characters other than brackets
def group_check2(s):
    print("group_check2 : " + s)
    matching = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in matching:
            stack.append(matching[c])
        elif not stack or c != stack.pop():
            return False
    if stack:
    
        return False
    return True
print( str(group_check2("()")) + "\n" )
print( str(group_check2("({")) + "\n" )
print( str(group_check2("({[]})")) + "\n" )
print( str(group_check2("(some)things in here")) + "\n" )
print( str(group_check2("begin(middle{ending )")) + "\n" )
print( str(group_check2("begin(middle{ending } } )")) + "\n" )
print( str(group_check2("begin(middle{ending } ) )")) + "\n" )
print( str(group_check2("(begin(middle{ending } ) )")) + "\n" )
    
    
    
print ("Kata : END ---------------- \n" )



print ("\nKata :  Find the vowels ---------- " )

#Description:
#We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).
#So given a string "super", we should return a list of [2, 4].
#
#Some examples:
#Mmmm  => []
#Super => [2,4]
#Apple => [1,5]
#YoMama -> [1,2,4,6]
#NOTE: Vowels in this context refers to English Language Vowels - a e i o u y
#NOTE: this is indexed from [1..n] (not zero indexed!)

def vowel_indices(s):
    matchingPositions = []

    matching = "aeiouy"
    print("vowel_indices received : \n" + s)
    for index, thisChar in enumerate(s):
        if thisChar.lower() in matching:
            matchingPositions.append(index + 1)
    return matchingPositions


print( str(vowel_indices("vowel_indices")) + "\n")
print( str(vowel_indices("Basic tests")) + "\n")
print( str(vowel_indices("super")) + "\n")


# from the solutions page
def vowel_indices2(word):
  return [i+1 for i,c in enumerate(word.lower()) if c in 'aeiou']
  
print( str(vowel_indices2("vowel_indices")) + "\n")
print( str(vowel_indices2("Basic tests")) + "\n")
print( str(vowel_indices2("super")) + "\n")



print ("Kata : END ---------------- \n" )







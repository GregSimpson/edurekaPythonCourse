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

print ("\nKata :  ---------------- " )





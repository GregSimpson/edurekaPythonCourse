# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:47:25 2016

@author: greg.simpson
"""

# Calculate the area of a box
class Box:
    def area(self):
        return self.width * self.height
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Create an instance of Box.
x = Box(10, 3)
# Print area.
print("Area of the box is : " + str(x.area()) + "\n\n")


#6. Write a program to calculate distance so that it 
# takes two Points (x1, y1) and (x2, y2) 
# as arguments and displays the calculated distance, 
# using Class.
import math
class Point:
    pass
first = Point()
second = Point()
first.x = float(input('Pls enter the x co-ordinate of the first point:'))
first.y = float(input('Pls enter the y co-ordinate of the first point:')) 

second.x = float(input('Pls enter the x co-ordinate of the second point:')) 
second.y = float(input('Pls enter the y co-ordinate of the second point:')) 

def dist(original,final):
    dist = math.sqrt((original.x - final.x) * (original.x - final.x) + (original.y - final.y) * (original.y - final.y))
    return dist

dist = dist(first, second)
print('Distance between two points ' + str(dist) + "\n\n")


#7. Correct the below program so that output should appear like this.
# [Expected output: x-value: 5 y-value: 7]
#Program:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):  
        return "x-value: " + str(self.x) + " y-value: " + str(self.y) 
    def __add__(self,other):
        p=Point()
        p.x = self.x+other.x
        p.y = self.y+other.y
        return p
p1 = Point(3,4)
p2 = Point(2,3)
print (p1+p2)
print("\n\n")



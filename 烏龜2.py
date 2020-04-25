# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:57:03 2020

@author: user
"""


import turtle
a=turtle.Turtle()
b=turtle.Screen()
b.title("My window")
b.bgcolor ('purple')
a.color ('white')
a.shape ('turtle')
c=0
while c<8:
    a.left(45)
    a.forward(100)
    c=c+1
turtle.done()    
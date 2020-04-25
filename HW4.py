# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:16:08 2020

@author: user
"""


import turtle
a=turtle.Turtle()
b=turtle.Screen()
b.title("My window")
b.bgcolor ('purple')
a.color ('white')
a.shape ('turtle')
a.pensize(5)
c=0
while c<360:
    a.left(1)
    a.forward(1)
    c=c+1
turtle.done()
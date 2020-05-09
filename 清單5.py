# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:00:21 2020

@author: user
"""


a=[]
sd=[]
b=int(input("請輸入學生數量:"))
for i in range(b):
    sde=input("請輸入學生姓名:")
    d=int(input("請輸入分數:"))
    a.append(d)
    sd.append(sde)
print(a)
##############
e=0
for i in range(b):
    e=e+a[i]
f=e/b
print("平均分數是:",f)
##################
g=0
h=100
for i in range(b):
    if a[i]>g:
        g=a[i]
        gn=i
    if a[i]<h:
        h=a[i]
        hn=i
print("最高分是:",g,"是:",sd[gn],"最低分是:",h,"是:",sd[hn])
        
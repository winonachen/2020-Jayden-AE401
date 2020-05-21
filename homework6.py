# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:26:18 2020

@author: user
"""


a=[]
b=int(input("請輸入學生數量:"))
student=[]
for i in range(b):
    sde=input("請輸入學生姓名:")
    c=int(input("請輸入分數:"))
    student.append(sde)
    student.append(c)
a.append(student)
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

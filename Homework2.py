# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:58:19 2020

@author: user
"""


a=input('請輸入你的數學成績:')
b=input('請輸入你的英文成績:')
a=int(a)
b=int(b)
if a>=90 and b>=90:
    print('恭喜！有獎品！')
elif a>60 and b>60:
    print('還可以')
elif a<60 and b>60:
    print('請再加油！')
elif b<60 and a>60:
    print('請再加油！')
else:
    print('嗚~！要處罰！')
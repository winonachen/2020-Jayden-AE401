# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:35:50 2020

@author: user
"""


import random
a=random.randint(1,5)
b=input("請猜一個數字：")
b=int(b)
print("答案是：",a)
if b==a:
    print("恭喜猜對了！")
else:
    print("你猜錯了！")

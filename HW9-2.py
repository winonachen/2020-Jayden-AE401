# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:05:24 2020

@author: user
"""


d={}
while True:
    key=input("請輸入單字,按0跳出:")
    
    if key=="0":
        print(d)
        break
    else:
        if key not in d.keys():
            value=input("請輸入翻譯:")
            d[key]=value
        else:
            print("此單字已經在字典裡了，請輸入其他單字!")
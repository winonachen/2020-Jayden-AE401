# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:19:43 2020

@author: user
"""


import radom
a=radom.randint(1,20)
c=0
while c<5:
      b=input ('請輸入一個數字:')
      b=int(b)
      if b==a:
         print ('恭喜答對了!')
         c=c+1
         break
      elif b>a:
         print("太大了!")
         b=input ('請再輸入一個數字:')
         b=int(b)
         b=b+1
         break
       else:
         print('太小了')
         b=input ('請再輸入一個數字:')
         b=int(b)
         b=b+1
         break
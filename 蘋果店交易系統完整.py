# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:02:45 2020

@author: user
"""


sellRecord=[]
while True:
    print("-------蘋果店交易系統-------")
    print("  1.設定庫存數量、單價")
    print("  2.進貨")
    print("  3.出貨/交易")
    print("  4.營業額統計")
    print("  5.庫存統計")
    print("  6.離開系統")
      
    function=int(input("請輸入欲使用功能選項之代號:"))
    
    print("-------------------------")

    if function==1:
        apple=int(input("現有庫存:") )
        price=int(input("單價:"))
        print("**************************")
        print("-------蘋果店交易系統--------")
        print(                  )
        print("現在庫存",apple,"顆蘋果")
        print("單價:一顆",price,"元")
        print("**************************")
    elif function==2:
        applein=int(input("進貨數量:"))
        apple=apple+applein
        print(                  )
        print("**************************")
        print("-------蘋果店交易系統--------")
        print(                  )
        print("進貨了",applein,"顆蘋果")
        print("現有",apple,"顆蘋果")
        print("**************************")
        
    elif function==3:
        appleout=int(input("交易蘋果數量:"))
        total=appleout*price
        apple=apple-appleout
        print("**************************")
        print("-------蘋果店交易系統--------")
        print(                  )
        print("交易數量:",appleout,"顆蘋果")
        print("應收金額:",total,"元")
        print("現有庫存:",apple,"顆蘋果")
        print(                  )
        print("**************************")
        sellRecord.append(appleout)
        
    elif function==4:
        total=0
        print("**************************")
        print("-------蘋果店交易系統--------")
        print(                  )
        print("目前交易紀錄:",)
        for i in range(len(sellRecord)):
            print(i+1,".賣出",sellRecord[i],"顆",sellRecord[i]*price,"元")
            total=total+(sellRecord[i]*price)
        print("總收入：", total,"元")
        print(                  )
        print("**************************")
    elif function==5:
        print("**************************")
        print("-------蘋果店交易系統--------")
        print(                  )
        print("現在庫存",apple,"顆蘋果")
        print(                  )
        print("**************************")
    elif function==6:
        print("********感謝使用本系統!********")
        break
    else:
        print("請輸入功能1~6喔！")
    
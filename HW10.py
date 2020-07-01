# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:39:32 2020

@author: user
"""


d={}

while True:
    
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    print("歡迎使用英文單字學習系統")
    print("---------------------")
    print("功能：")
    print("1. 建立字彙表")
    print("2. 列出全部單字")
    print("3. 英翻中")
    print("4. 中翻英")
    print("5. 測驗學習成果")
    print("6. 離開系統")
    
    print("---------------------")
    #輸入要使用的功能
    function=input("請輸入要使用的功能之代號:")
    
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    if function == "1":
            while True:    
                key=input("請輸入單字(按0跳出)：")
                if key == "0" : #輸入為0時跳出。鍵盤輸入的是字串，所以判斷用的0也要當字串                 
                    break         
                else:            
                    if key not in d:
                        value=input("請輸入中文翻譯：")
                        d[key]=value
                    else:
                        print("此單字已在字典中，請輸入其他單字！")
    elif function == "2":
        print("目前單字庫：----------------")
        #印出單字庫所有單字以及對應中文
        for k,v in d.items():
            print(k,"：",v)
    elif function == "3":
        while True:
            #請輸入要翻譯的英文(按0跳出)：
            k=input("請輸入要翻譯的英文(按0跳出)：")
            if k == str(0):
                break
            else:
                #如果輸入的 K不在字典中....
                if k not in d:
                    print("此單字未在字典中喔！請重新輸入")
                else:
                    #k有出現在字典d中，那就印出他的對應中文
                    print("中文：", d[k])
    elif function == "4":
        
        while True:
            found = False #確認是否找到單字用
            ch = input("請輸入要翻譯的中文(按0跳出)：")        
            if ch == str(0): #輸入為0時，跳出
                break
            
            else:
                #找尋所有字典中的英文
                for k,v in d.items(): 
                    #如果有輸入的中文，就印出對應的英文
                    if ch == v :
                        print("英文：",k)
                        found=True
            if not found: 
                    print("此單字未在字典中喔！請重新輸入")
    elif function == "5":
       score=0
       for k,v in d.items():
           print("中文:",v)
           ans=input("答案:")
       if ans == k:
           score = score + 1
           print("答對了!，目前分數是:",score)
           print("---------------------")
       else:
           print("答錯了!，目前分數是:",score)
           print("---------------------")
       print("測驗結束!你的分數是:",score)
    elif function == "6":
        print("感謝使用本系統!")
        break
    else:
        print("功能選項輸入錯誤，請重新輸入!")
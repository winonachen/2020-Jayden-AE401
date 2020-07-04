# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:32:29 2020

@author: user
"""


d={}

########新增#########
import os.path #匯入os.path函式庫

if not os.path.isfile("vocabulary.txt"): #先判斷有沒有字彙表的txt檔
    file=open("vocabulary.txt","w") #沒有則建立新的字彙表，open(檔名,模式)，寫入模式為"w"
    print("create new vocabulary.txt...")
else:
    file=open("vocabulary.txt","r") #如果有vocabulary.txt文件檔則讀取檔案
    r=file.read()
    print("open old vocabulary.txt...")
    print(r)
    
file.close() #關閉文件檔
####################

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
    function=input("請輸入要使用的功能選項：")
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    
    
    if function == "1":
        while True:    
            key=input("請輸入單字(按0跳出)：")
            if key == str(0): #鍵盤輸入的是字串，所以判斷用的0也要當字串                 
                break         
            else:            
                if key not in d:
                    value=input("請輸入中文翻譯：")
                    d[key]=value
                else:
                    print("此單字已在字典中，請輸入其他單字！")   
                    
        ######新增#######
        file=open("vocabulary.txt","a") #將剛新增至字典的字彙，加入txt檔內紀錄(加入模式="a")
        
        for k,v in d.items():     #把字典中的key跟value都寫入txt文件檔裡                                           
            file.write(k)
            file.write(":")
            file.write(v)
            file.write("\n") #換行
        
        file.close() #關閉文件檔
        ################    
                    
    elif function == "2":
        print("目前單字庫：----------------")
        #for k,v in d.items():
         #  print(k,":",v)
        ###########新增############# 
        file=open("vocabulary.txt","r") #讀取文件檔內資料，read模式 = "r"
        print(file.read())
        file.close()#關閉文件檔
        ############################
    
    elif function == "3":
        while True:
            k=input("請輸入要翻譯的英文(按0跳出)：")
            if k == str(0):
                break
            else:
                if k not in d:
                    print("此單字未在字典中喔！請重新輸入")
                else:
                    print("中文：", d[k])
                    
    elif function == "4":
        
        while True:
            found = False #確認是否找到單字用
            ch = input("請輸入要翻譯的中文(按0跳出)：")        
            if ch == str(0):
                break
            
            else:            
                for k,v in d.items(): 
                    if ch == v:
                        print("英文：", k)
                        found=True
            if not found: 
                    print("此單字未在字典中喔！請重新輸入")
                    
    elif function == "5":
        score=0
        for k,v in d.items():
            print("中文：",v)
            ans=input("英文：")
            if ans == k:
                score = score + 1
                print("答對了！，目前分數是", score)
                print("-")
            else:
                print("答錯了！，目前分數是", score)
                print("-")
        print("測驗結束，你的分數是：", score)
    elif function == "6":
        break
    
    else:
        print("功能選項輸入錯誤！請重新輸入！")
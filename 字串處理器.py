# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:37:00 2020

@author: user
"""


import os.path

content=""#內容字串變數定義為空的，清除之前記憶

while True:
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    print("歡迎使用字串處理器")
    print("---------------------")
    print("功能：")
    print("1. 輸入檔案")
    print("2. 單字統計表")
    print("3. 查詢檔案中單字")
    print("4. 替換檔案中單字")
    print("5. 離開系統")
    print("---------------------")
    function=input("請輸入要使用的功能選項：")
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")

    ### 功能一 ##########################    
    if function=="1":        
        fileName=input("請輸入檔名(含副檔名):")#變數儲存輸入檔名(含副檔名)(input)        
        if os.path.isfile(fileName):            
            file=open(fileName,"r")#打開文件,讀取模式(open)
            content=file.read()#讀取文件內容(read)
            print("\n",content)#印出檔案內容

        else:            
            print("沒有此文件！") 

        file.close()#關閉文件(close)

    ### 功能二 ##########################
    elif function=="2":          
        if content: #如果有內容變數(True)，表示有讀取到內容
            wordList=content.split() #分割字串(split)
            print("文件共有",len(wordList),"個字") #印出文件共有幾個字(len)
        else:
            print("沒有內容！請先輸入檔案！")

    ### 功能三 ##########################     
    elif function=="3":            
        wordCount=0#單字計數預設為0

        if content:   #如果有內容變數(True)，表示有讀取到內容
            searchWord=input("請輸入要搜尋的單字：")#輸入搜尋單字(input)
            wordCount=fileName.count(fileName)#計算字串中單字數量(count)
            print(searchWord,"共出現了",wordCount,"次") #印出單字共出現了幾次(print)

        else:
            print("沒有內容！請先輸入檔案！")

    ### 功能四 ##########################            
    elif function=="4":                 
        if content:   #如果有內容變數(True)，表示有讀取到內容
            oldWord=input("請輸入要替換的單字：")#輸入要替換的單字
            newWord=input("請輸入新的單字：")#輸入新的單字
            content=content.replace(oldWord,newWord)#用字串取代(replace)
            print("更新後內容：\n",content)#內容變數 )
            file=open(fileName,"w")#打開文件,寫入模式
            file.write(content)#更新寫入新字串
            file.close()#關閉文件
        else:
            print("沒有內容！請先輸入檔案！")

    ### 功能五 ##########################              
    elif function=="5":
        print("離開系統...")
        break#離開while迴圈

    else:
        print("輸入錯誤！請重新輸入！") 
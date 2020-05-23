a=[]
b=int(input("請輸入學生數量:"))
for i in range(b):
    d=int(input("請輸入分數:"))
    a.append(d)
print(a)
##############
hight=max(a)
lost=min(a)
c=sum(a)/b
print("最高分是:",hight)
print("最低分是:",lost)
print("平均是:",c)        
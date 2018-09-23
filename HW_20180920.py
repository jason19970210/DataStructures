# -*- coding: utf-8 -*-

import datetime

i = 0
convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# --- def ---
# --- 遞迴 ---
def convD(n,b):
    
    if n < b:
        return convertString[n]
    else:
        return convD(n//b,b) + convertString[n%b]


# --- 迴圈 ---
def convH(n,b):
    
    q = n / b
    r = n % b
    







# --- Loop for 5 inputs & results ---
while i < 5:
    
    i += 1
    print("第",i,"筆資料")
    
    n = int(input("請輸入十進制正整數: "))
    b = int(input("base: "))
    
    
    tStartD = datetime.datetime.now()
    print(n,"(10) ->",convD(n,b),"(",b,")")
    tEndD = datetime.datetime.now()
    print ("遞迴轉換運行時間: ",tEndD - tStartD, "\n")

import time

n = int(input("請輸入十進制: "))
b = int(input("請輸入欲轉換進制: "))
convertString = "0123456789ABCDEFGHIJKLMNOP"


tStartD = time.time()



def convD(n,b):
    
    if n < b:
        return convertString[n]
    else:
        return conv(n//b,b) + convertString[n%b]
    
    
print(convD(n,b))
tEndD = time.time()
print (tEndD - tStartD)
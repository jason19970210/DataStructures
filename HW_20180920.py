import time

n = int(input("請輸入十進制正整數: "))
b = int(input("base: "))
convertString = "0123456789ABCDEFGHIJKLMNOP"


tStartD = time.time()


def convD(n,b):
    
    if n < b:
        return convertString[n]
    else:
        return convD(n//b,b) + convertString[n%b]
    

#str = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(n,"(10) ->",convD(n,b),"(",b,")")
tEndD = time.time()
print ("Cost ",tEndD - tStartD," sec")
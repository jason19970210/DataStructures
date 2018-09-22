import time

n = int(input("請輸入十進制正整數: "))
b = int(input("base: "))
convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#tStartD = time.time()


def convD(n,b):
    
    if n < b:
        return convertString[n]
    else:
        return convD(n//b,b) + convertString[n % b]

def convH(n,b):

    while currentn != 0:
        return
        
        




#str = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print("遞迴轉換:  ",n,"(10) ->",convD(n,b),"(",b,")")
print("迴圈轉換:  ",n,"(10) ->",convH(n,b),"(",b,")")
#tEndD = time.time()
#print ("Cost ",tEndD - tStartD," sec")

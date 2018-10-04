import datetime

def hanoi(n, A, B, C):
    if n == 1:
        return [(A, C)]
    else:
        return hanoi(n-1, A, C, B) + hanoi(1, A, B, C) + hanoi(n-1, B, A, C)

    

#n = input("請輸入整數：")
n = 3

while n < 25:
    print(n,"個盤子")
    m = 0
    tStart = datetime.datetime.now()
    for move in hanoi(int(n), 'A', 'B', 'C'):
        #print("盤由 %c 移至 %c" % move)
        m = m + 1
    tEnd = datetime.datetime.now()
    print(m,"個步驟")
    print("運行時間: ",tEnd - tStart, "\n")
    n = n + 5
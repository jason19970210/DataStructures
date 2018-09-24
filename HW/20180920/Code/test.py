#!/usr/bin/python
# -*- coding:utf-8 -*-

n = int(input("請輸入十進制正整數: ")) 
b = int(input("請輸入欲轉換進制: "))
q = ''
convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


''' reverse string
a = '11223344'
r = list(a)
r.reverse()
print(''.join(r))
'''

'''
n = 100
str(n)
output : '100'
'''
while n > 0:
    if n >= b:
        q += convertString[n%b]
        n = n // b
        
        print("n = ",n)
        print("q = ",q)
    elif n // b < b:
        q += convertString[n%b]
        print(q)
        r = list(q)
        r.reverse()
        print(''.join(r))
        break

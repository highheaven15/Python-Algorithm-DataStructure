#02. 숫자만 추출

import sys
sys.stdin=open("input.txt", "rt")

s=input()

num=0
for x in s:
    if x.isdecimal()==True:
        num=10*num+int(x)
print(num)

cnt=0
for i in range(1, num+1):
    if num % i ==0:
        cnt +=1
print(cnt)

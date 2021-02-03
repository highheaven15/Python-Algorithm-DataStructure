#06. 격자판 최대합

import sys
sys.stdin=open("input.txt", "rt")

n =int(input())

a=[list(map(int, input().split())) for _ in range(n)]

#for x in a: #이렇게 하면 격자 모양으로 볼수있다.
#   print(x)
largest=-2174000000

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        lastgest=sum2

sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    lastgest=sum2
    
print(largest)

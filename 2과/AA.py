import sys
sys.stdin=open("input.txt", "rt")

import random
n, k = map(int, input().split())
a=list(map(int, input().split()))
random.shuffle(a)


b=[1,2,3,4,5,6,7]
d=[]
for i in range(6):
    for j in range(6):
        for k in range(6):
            c= b[i]+b[j]+b[k]
            d.append(c)

print(c)

print(a)

#03. K번째 큰 수

import sys
sys.stdin=open("input.txt", "rt")

import random
n, k = map(int, input().split())
a=list(map(int, input().split()))

#강의 풀이

#3개 숫자를 더한값이 중복될수가 있다
#리스트는 중복값도 계속 입력되게 된다=>set자료구조형 이용

res =set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])


res=list(res)
res.sort(reverse=True)
print(res[k-1])

#나의 풀이 

d=[]

for i in range(n):
    for j in range(n):
        for l in range(n):
            if i<j and j<l:
                c= a[i]+a[j]+a[l]   
                
                d.append(c)
                
e=list(set(d))

e.sort(reverse=True)

print(e[k-1])

#05. 정다면체

import sys
sys.stdin=open("input.txt", "rt")

n, m= list(map(int, input().split()))

#강의 풀이
cnt =[0]*(n+m+3)
max= -21470000000 #초기 최대값 설정

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(n+m+1): 
    if cnt[i] >max: #최댓값을 지정해 준뒤
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i] ==max: #최댓값과 같은 인덱스 찾아오기
        print(i, end=" ")


#나의 풀이
'''
cnt=[0]*(n+m+3)

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
        
print(max(cnt))


for k in range(1, n+m+1):
    if cnt[k] ==max(cnt): #list의 최댓값을 바로 찾은 경
        print(k, end=" ")
'''

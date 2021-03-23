#06. 응급실

import sys
sys.stdin=open("input.txt", "rt")

from collections import deque

n, m=map(int, input().split())

dq=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]

dq=deque(dq)

cnt=0

while True:
    cur=dq.popleft()
    if any(cur[1] < x[1] for x in dq): #any() 함수는 for문 돌면서 단 한개라도 참이면 그 순간 return True하고 멈춘다
        dq.append(cur)
    else: #any조건을 만족하지 못한 경우 즉 cur[1]이 다른것들보다 가장 큰 경우, 위험도가 가장 높음
        cnt+=1
        if cur[0]==m:
            break
print(cnt)

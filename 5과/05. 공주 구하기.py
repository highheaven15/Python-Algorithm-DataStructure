#05. 공주 구하기
import sys
sys.stdin=open("input.txt", "rt")

#deque자료 구조형
#리스트는 pop() 하면 밀리는 연산이 있고, deque는 없습니다.

#강의 풀이

from collections import deque
n, k=map(int,input().split())

dq=list(range(1, n+1)) #리스트 생성

dq=deque(dq) #deque함수를 통해 deque자료구조로 바꿔줘

while dq: #빌때까지 계속 돈다
    for _ in range(k-1): #k-1바퀴를 돌겠다는 의미
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft() #k번째 요소 제거
    if len(dq)==1:
        print(dq[0])
        dq.popleft() #dq를 비우므로써 while문을 종료시킨다.
'''
#나의 풀이
N, K=map(int,input().split())

que=[]
for i in range(1, N+1): #[1, 2, 3, 4, 5, 6, 7, 8]
    que.append(i)

cnt=0

while True:        
    que.append(que.pop(0))
    cnt+=1
    if cnt==K:
        que.pop()
        cnt=0
    if len(que)==1:
        break
print(que[0])
'''

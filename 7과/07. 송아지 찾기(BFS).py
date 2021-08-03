#07. 송아지 찾기(BFS)

import sys
from collections import deque
sys.stdin=open("input.txt", "r")

MAX=10000
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)

n, m = map(int, input().split())

ch[n]=1
dis[n]=0

dQ=deque()
dQ.append(n) #출발점 추가

while dQ:
    now=dQ.popleft() #dQ에서 하나 pop시킴
    if now==m:
        break
    
    for next in(now-1, now+1, now+5): #next가 3바퀴 돈다.
        if 0<next<=MAX:
            if ch[next]==0: #방문을 안한것이 확인되면
                dQ.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])

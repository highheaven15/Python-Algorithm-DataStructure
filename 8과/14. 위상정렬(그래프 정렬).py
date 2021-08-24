#14. 위상정렬(그래프 정렬)
#답이 여러가지이므로 채점폴더에는 없다

#일의 선후관계가 있다

#연결된 간선의 개수 =차수라고 한다.들어오는 간선은 진입차수
import sys
sys.stdin=open("input.txt", "rt")
from collections import deque

n, m =map(int, input().split()) 
graph=[[0]*(n+1) for _ in range(n+1)]
degree=[0]*(n+1) #진입차수
dQ=deque()
for i in range(m):
    a, b=map(int, input().split())
    graph[a][b]=1 #방향 그래프
    degree[b]+=1
for i in range(1, n+1):
    if degree[i]==0: #선행작업이 없는경우
        dQ.append(i)

while dQ:
    x=dQ.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
        if graph[x][i]==1:
            degree[i]-=1
            if degree[i]==0:
                dQ.append(i)

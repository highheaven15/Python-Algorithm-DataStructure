#15. 토마토(BFS)

#최단거리로 퍼져나가는 문제는 DFS로 풀면 안되고 BFS로 풀어야 합니다. 
import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)

from collections import deque

dx=[-1, 0 ,1, 0]
dy=[0, 1, 0, -1]

m, n=map(int, input().split()) #m은 가로, n은 세로
board=[list(map(int, input().split())) for _ in range(n)]
dis=[[0]*m for _ in range(n)]
Q=deque()

for i in range(n):
    for j in range(m):
        if board[i][j]==1: #여기는 다른 문제와는 다르게 1인거 다 Q에 넣고 같이 시작
            Q.append((i, j))

while Q:
    tmp=Q.popleft()
    for k in range(4):
        x=tmp[0]+dx[k]
        y=tmp[1]+dy[k]
        if 0<=x<n and 0<=y<m and board[x][y]==0:
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x, y))

flag=1
for a in range(n):
    for b in range(m):
        if board[a][b]==0:
            flag=0
result=0
if flag==1:
    for a in range(n):
        for b in range(m):
            if dis[a][b]>result:
                result=dis[a][b]
    print(result)
else:
    print(-1)
    
''' 이것도 가능함
for a in range(n):
    for b in range(m):
        if board[a][b]==0:
            print(-1)
            sys.exit(0)
result=0         
for a in range(n):
    for b in range(m):
        if dis[a][b]>result:
            result=dis[a][b]
print(result)
'''

#14. 안전영역(DFS, BFS)

#DFS 풀이
import sys
sys.stdin=open("input.txt", "r")
dx=[-1, 0 ,1, 0]
dy=[0, 1, 0, -1]

sys.setrecursionlimit(10**6) #파이썬에서 재귀를 돌때..
#파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다.필수코드

def DFS(x, y, h):
    ch[x][y]=1 #방문했다고 체크
    for k in range(4):
        xx=x+dx[k]
        yy=y+dy[k]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
            DFS(xx, yy, h)
    
if __name__=="__main__":
    n=int(input())
    cnt=0 #정한 높이
    res=0
    board=[list(map(int, input().split())) for _ in range(n)]
    for h in range(100): #a위치 #높이를 0부터 99까지
        ch=[[0]*n for _ in range(n)] #체크 리스트
        cnt=0
        for i in range(n):
            for j in range(n):
                if board[i][j]>h and ch[i][j]==0:#물에 잠기지않은 구역 발견
                    cnt+=1
                    DFS(i, j, h)
        res=max(res, cnt) #cnt의 최대값 찾기 위해..
        if cnt==0: #board의 최대 높이를 넘어가는 경우는 안전지역이 0개가된다.
            break #a위치의 for문을 멈춘다.
    print(res)


#BFS 풀이

import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)

from collections import deque

dx=[-1, 0 ,1, 0]
dy=[0, 1, 0, -1]
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt=0
res=0
Q=deque()
for h in range(100):
    ch=[[0]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if board[i][j]>h and ch[i][j]==0:
                ch[i][j]=1
                Q.append((i, j))

                while Q:
                    tmp=Q.popleft()
                    for k in range(4):
                        x=tmp[0]+dx[k]
                        y=tmp[1]+dy[k]
                        if 0<=x<n and 0<=y<n and board[x][y]>h and ch[x][y]==0:
                            ch[x][y]=1
                            Q.append((x, y))
                cnt+=1
    if cnt==0:
        break
    res=max(res, cnt)
print(res)

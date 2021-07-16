#15. 경로탐색(그래프 DFS)

#한번 방문한 노드는 다시 방문해서는 안된다.

import sys
sys.stdin = open("input.txt", "rt")
#원래 문제 + 경로까지 구해본 코드
def DFS(v):
    global cnt
    if v==n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1): #1~5
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0


if __name__=="__main__":
    n, m = map(int, input().split()) # n=5, m=9
    g=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)

    for i in range(m):
        a, b = map(int, input().split())
        g[a][b]=1
        
    cnt=0
    path=[]
    path.append(1)
    ch[1]=1
    DFS(1)
    print(cnt)

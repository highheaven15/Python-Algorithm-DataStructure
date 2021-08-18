#17. 피자 배달 거리(DFS)

import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)

def DFS(L, s):
    global res
    if L==m:
        sum=0
        for j in range(len(hs)):
            x1=hs[j][0]
            y1=hs[j][1] #집이 정해짐
            dis=2147000000
            for x in cb: #조합의 경우의 수에서 ex)(0, 1, 2, 3)
                x2=pz[x][0]
                y2=pz[x][1] #피자집이 정해짐
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum<res:
            res=sum

    else:
        for i in range(s, len(pz)):
            cb[L]=i
            DFS(L+1, i+1) #조합구하기-피자집 선택


if __name__=="__main__":
    n, m=map(int, input().split())
    board=[list(map(int, input().split())) for _ in range(n)]
    hs=[] #집좌표
    pz=[] #피자집 좌표
    cb=[0]*m #조합의 경우의 수 저장
    res=2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i, j))
            elif board[i][j]==2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)

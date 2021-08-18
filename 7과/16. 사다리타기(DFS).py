#16. 사다리타기(DFS)
import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)

def DFS(x, y):
    ch[x][y]=1
    if x==0: #맨 위까지 오면
        print(y) #열 번호 출력
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else: #왼쪽 오른쪽 둘다 못가면 위로 올라감
            DFS(x-1, y)

if __name__=="__main__":
    board=[list(map(int, input().split())) for _ in range(10)]
    ch=[[0]*10 for _ in range(10)]
    for y in range(10): #열번호
        if board[9][y]==2: #체크 리스트 
            DFS(9, y) #사다리 아래 지점부터 위로 탐색

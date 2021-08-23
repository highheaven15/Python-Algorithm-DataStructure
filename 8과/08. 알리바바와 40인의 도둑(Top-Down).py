#08. 알리바바와 40인의 도둑(Top-Down)

import sys
sys.stdin=open("input.txt", "r")
def DFS(x, y):

    if dy[x][y]>0: #기록된 값이 존재하면
        return dy[x][y]
    
    if x==0 and y==0:
        return arr[0][0]
    else:
        if y==0:
            dy[x][y]=DFS(x-1,y)+arr[x][y] 
        elif x==0:
            dy[x][y]=DFS(x, y-1)+arr[x][y]
        else:
            dy[x][y]=min(DFS(x-1, y), DFS(x, y-1)) +arr[x][y]
        return dy[x][y] #메모리제이션을 위해 dy[x][y]에 저장
if __name__=="__main__":
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)] #메모리제이션을 위해 생성
    print(DFS(n-1, n-1))

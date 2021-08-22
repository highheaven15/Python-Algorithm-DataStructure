#06. 가장 높은 탑 쌓기

import sys
sys.stdin = open("input.txt", "rt")

n=int(input())
bricks=[]
for i in range(n):
    a, b, c=map(int, input().split())
    bricks.append((a, b, c))
bricks.sort(reverse=True) #벽돌 넓이에 대해 내림차순 정렬
dy=[0]*n
dy[0]=bricks[0][1]
res=bricks[0][1]
for i in range(1, n):
    max_h=0
    for j in range(i):
        if bricks[i][2]<bricks[j][2] and dy[j]>max_h:
            max_h=dy[j]
    dy[i]=max_h+bricks[i][1]
    res=max(res,dy[i])
print(res)

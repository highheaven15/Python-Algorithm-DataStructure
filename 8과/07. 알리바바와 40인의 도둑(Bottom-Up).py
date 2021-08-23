#07. 알리바바와 40인의 도둑(Bottom-Up)

import sys
sys.stdin=open("input.txt", "r")

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
dy=[[0]*n for _ in range(n)]

dy[0][0]=arr[0][0] #초기화

for i in range(1,n):
    dy[0][i]=dy[0][i-1]+arr[0][i]
    dy[i][0]=dy[i-1][0]+arr[i][0]

for i in range(1, n):
    for j in range(1, n):
        #if dy[i-1][j]>=dy[i][j-1]:
        #    dy[i][j]=dy[i][j-1]+arr[i][j]
        #else:
        #    dy[i][j]=dy[i-1][j]+arr[i][j]
        dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]
print(dy[n-1][n-1])

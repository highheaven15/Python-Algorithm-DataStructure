#09. 봉우리

import sys
sys.stdin=open("input.txt", "rt")

n =int(input())

a=[list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0]*n)
a.append([0]*n)

for x in a: #각 행에 접근, x는 각 행, 1차원리스트를 의미
    x.insert(0, 0)
    x.append(0)
    
for x in a:
    print(x)

###입력완료상태

cnt=0

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

for i in range(1, n+1): #0번은 가장자리이므로
    for j in range(1, n+1):
        if all(a[i][j] > a[i + dx[k]][j+dy[k]] for k in range(4)):
            cnt +=1
'''
for i in range(1,n+1):
    for j in range(1, n+1):
        if(a[i][j] > max(a[i-1][j], a[i][j-1], a[i+1][j], a[i][j+1])):
            cnt+=1
'''

print(cnt)

#13. 회장뽑기(플로이드-워샬 응용)

import sys
sys.stdin = open("input.txt", "rt")

n=int(input())
dis=[[100]*(n+1) for _ in range(n+1)] #큰 값으로 초기화
for i in range(1, n+1):
    dis[i][i]=0
    
while True:
    a, b=map(int, input().split())
    if a==-1 and b==-1:
        break
    dis[a][b]=1 #무방향 그래프
    dis[b][a]=1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j]) #플로이드 워셜

res=[0]*(n+1)
score=100
for i in range(1, n+1):
    for j in range(1, n+1):
        res[i]=max(res[i], dis[i][j])
    score=min(score, res[i])
out=[]
for i in range(1, n+1):
    if res[i]==score:
        out.append(i)
print("%d %d" %(score, len(out)))

for x in out:
    print(x, end=' ')
''' 내 풀이 이것도 맞음            
res=[0]*(n+1)
for i in range(1, n+1):
    for j in range(1, n+1):
        res[i]=max(res[i], dis[i][j])

print(min(res[1:]), res.count(min(res[1:])))
for i in range(1, n+1):
    if res[i]==min(res[1:]):
        print(i, end=' ')
'''







    

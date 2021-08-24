#12. 플로이드 워샬 알고리즘

#그래프에서 모든 정점에서 모든 정점으로 가는 최단거리의 최단거리
#dis는 인접행렬로 초기화!
#dis[i][k] : 정점 i-> 정점 j로 가는데 드는 최소비용
#Q1. 오름차순으로만 되는것이냐?
#A1. 2->1->4->3->도 가능
#Q2. 5->3->4가는 과정에서 앞 5->3에 이미 3이 적용되서 중복적용아니냐?
#A2. 3->3(값 0)이라 상관없다.


import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
dis=[[5000]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):#i->i로 가는거 0으로 초기화
    dis[i][i]=0
    
for i in range(m): #인접 행렬 초기화
    a, b, c= map(int, input().split())
    dis[a][b]=c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j]==5000:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()

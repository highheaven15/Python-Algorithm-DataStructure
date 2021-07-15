#14. 인접행렬(가중치 방향그래프)

#그래프 : 노드 + 간선의 집합
#방향그래프 : 간선에 방향이 설정
#가중치 방향그래프 : 간선의 값까지 설정

#노드사이에 방향없이 선이 연결됨 = 에지(edge)
#노드사이에 방향있이 선이 연결됨 = 아크(arc)

import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split()) #n=5

g=[[0]*(n+1) for _ in range(n+1)] #칸은 6x6이 나온다.

for i in range(m):
    a, b, c=map(int, input().split())
    g[a][b]=c
    #g[b][a]=c 무방향의 그래프의 경우 추가 필요
    
for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print() #5x5가 나온다.

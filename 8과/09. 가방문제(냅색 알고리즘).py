#09. 가방문제(냅색 알고리즘)

import sys
sys.stdin = open("input.txt", "rt")

n, m=map(int, input().split()) #보석의 종류, 무게의 한계값
dy=[0]*(m+1) #dy[j] : 가방에 j무게만큼 담을때의 보석의 최대가치
for i in range(n):
    w, v=map(int, input().split()) #보석의 무게, 보석의 가치
    for j in range(w, m+1):
        dy[j]=max(dy[j], dy[j-w]+v)
print(dy[m])

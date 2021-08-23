#11. 최대점수 구하기(냅색 알고리즘)

#한유형당 한번만 풀수있다는 것이 앞문제와의 차이점

import sys
sys.stdin = open("input.txt", "rt")

n, m=map(int, input().split())
dy=[0]*(m+1)
for i in range(n):
    ps, pt=map(int, input().split())
    for j in range(m, pt-1, -1): #거꾸로 가자. 정방향으로 했더니 오류나네
        dy[j]=max(dy[j], dy[j-pt]+ps)
print(dy[m])

#10. 동전교환(냅색 알고리즘)

import sys
sys.stdin = open("input.txt", "rt")

n=int(input())
coin=list(map(int, input().split())) 
m=int(input())
dy=[1000]*(m+1) #dy[j] : j원을 거슬러 주는데 사용된 동전의 최소 개수
#큰 값으로 초기화 해줘야한다.
dy[0]=0
for i in range(n):
    for j in range(coin[i],m+1):
        dy[j]=min(dy[j],dy[j-coin[i]]+1)
print(dy[m])

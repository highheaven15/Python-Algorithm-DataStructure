#01. 동적계획법이란? 네트워크 선 자르기(Bottom-Up)

#큰 크기의 복잡한 문제를 속성은 유지하면서 작은 단위로 축소시켜 답을 구하고
#약간 더 큰 문제로 확장, 앞의 답을 이용해가면서 범위를 확장해 나간다.(점화식)
#문제를키워나가는 것 =Bottom-Up적 Dynamic Programming

import sys
sys.stdin = open("input.txt", "rt")

n=int(input())
dy=[0]*(n+1)
dy[1]=1 #직관적으로 알수있는 것들은 초기
dy[2]=2
for i in range(3, n+1):
  dy[i]=dy[i-2]+dy[i-1]

print(dy[n])

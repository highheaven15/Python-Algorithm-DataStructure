#05. 최대 선 연결하기(LIS 응용)
#다른 문제 같은 내용 
#Q1. 선을 다 연결해두고 최소 몇개의 선을 제거하면 교차하지 않으면서 선을 가장 많이 남길수있는가?
#A1.전체 선수-최대부분 증가 수열 수

#Q2.다리를 만드는데 교차불가능하며, 최대 만들수 있는 다리의 개수
#A2.전체 다리수-최대부분 증가 수열 수

import sys
sys.stdin = open("input.txt", "rt")

n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1 #마지막 항이 arr[1]인 경우 최대 증가수열의 길이
res=0 #최댓값

for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max: #마지막항보다 작은 숫자를 찾기
            max=dy[j] #가장큰 경우에만
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i] #최대값 찾기
print(res)

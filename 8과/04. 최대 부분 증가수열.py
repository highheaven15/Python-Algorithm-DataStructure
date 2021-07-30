#04. 최대 부분 증가수열

import sys
sys.stdin = open("input.txt", "rt")

n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1 #마지막 항이 arr[1]인 경우 최대증가수열의 길이
res=0 #최댓값

for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max: #마지막항보다 작은 숫자를 찾기
            max=dy[j] #가장 큰 경우에만
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i] #최대값 찾기
print(res)

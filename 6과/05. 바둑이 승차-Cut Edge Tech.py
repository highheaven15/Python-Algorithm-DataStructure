#05. 바둑이 승차-Cut Edge Tech

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, sum, tsum): #L은 인덱스 번호, sum은 합

    global result #전역변수 result 설정

    if sum+(total-tsum)<result:
        return
    if sum>c: #합이 c를 넘지못하면 종료
        return
    if L==n: #종료지점에 도달
        if sum>result:
            result=sum #지역변수 result가 아니므로
    else:
        DFS(L+1, sum+a[L], tsum+a[L]) #부분집합으로 참여시킴
        DFS(L+1, sum, tsum+a[L])      #부분집합으로 참여 안시킴
    


if __name__=="__main__":
    c, n = map(int, input().split())
    a=[0]*n
    result=-2147000000 #가장작은 값으로 초기화
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0, 0, 0)
    print(result)

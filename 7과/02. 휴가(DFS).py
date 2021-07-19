#02. 휴가(DFS)

import sys
sys.stdin = open("input.txt", "rt")

#강의 풀이

def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    T=list()
    P=list()
    for i in range(n):
        a, b=map(int, input().spilt())
        T.append(a)
        P.append(b)
    res=-2147000000
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)
    print(res)

#나의 풀이
def DFS(L, profit):
    global maxprofit
    if L>n:
        return
    if L==n:
        if profit>maxprofit:
            maxprofit=profit
    else:
        DFS(L+schedule[L][0], profit+schedule[L][1])
        DFS(L+1, profit)
            

if __name__=="__main__":
    n=int(input()) #n=7
    schedule=[]
    maxprofit=-2147000000
    for _ in range(n):
        t,p=map(int, input().split())
        schedule.append((t, p))
    DFS(0,0)
    print(maxprofit)

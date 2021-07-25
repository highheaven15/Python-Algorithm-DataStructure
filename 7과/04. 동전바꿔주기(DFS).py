#04. 동전바꿔주기(DFS)

#강의 풀이

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, sum):
    global cnt
    if sum>T:
        return
    if L==k:
        if sum==T:
            cnt+=1
    else:
        for j in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*j))
            
if __name__=="__main__":
    T=int(input()) #지폐의 금액
    k=int(input()) #동전의 가지수
    cv=list()
    cn=list()
    for i in range(k):
        p, n=map(int, input().split())
        cv.append(p)
        cn.append(n)
    cnt=0
    DFS(0, 0)
    print(cnt)

#나의 풀이
    
def DFS(L, sum):
    global cnt
    if sum>T:
        return
    if L==k:
        if sum==T:
            cnt+=1
    else:
        for j in range(coin[L][1]+1):
            DFS(L+1, sum+(coin[L][0]*j))

if __name__=="__main__":
    T=int(input()) #지폐의 금액
    k=int(input()) #동전의 가지수
    coin=[]
    for i in range(k):
        p, n=map(int, input().split())
        coin.append((p, n))
    cnt=0
    DFS(0, 0)
    print(cnt)

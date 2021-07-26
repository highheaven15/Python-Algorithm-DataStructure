#05. 동전 분배하기(DFS)

import sys
#sys.stdin = open("input.txt", "rt")

#강의 풀이

def DFS(L):
    global smallest
    if L==n:
        cha=max(money)-min(money)
        if cha<smallest:
            tmp=set() #집합 자료구조형, 중복 제거
            for x in money:
                tmp.add(x)
            if len(tmp)==3:#길이가 3, 즉 money가 다 다른 경우
                smallest=cha
    else:
        for i in range(3):
            money[i]+=a[L] #돈을 더해주는 경우
            DFS(L+1)
            money[i]-=a[L] #돈 더해준거를 다시 되돌리는 경우
            
if __name__=="__main__":
    n=int(input())
    a=[]
    money=[0]*3
    for i in range(n):
        a.append(int(input())) #[8, 9, 11, 12, 23, 15, 17]
    smallest=2147000000
    DFS(0)
    print(smallest)

#나의 풀이
    
def DFS(L, s1, s2, s3):
    global smallest
    if L==n:
        if s1!=s2 and s1!=s3 and s2!=s3:
            k=max(s1, s2, s3)-min(s1, s2, s3)
            if k<smallest:
                smallest=k
    else:
        DFS(L+1, s1+a[L], s2, s3)
        DFS(L+1, s1, s2+a[L], s3)
        DFS(L+1, s1, s2, s3+a[L])
        
            
if __name__=="__main__":
    n=int(input())
    a=[]
    for i in range(n):
        a.append(int(input())) #[8, 9, 11, 12, 23, 15, 17]
    smallest=2147000000
    DFS(0, 0, 0, 0)
    print(smallest)

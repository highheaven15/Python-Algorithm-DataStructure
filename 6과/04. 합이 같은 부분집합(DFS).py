#04. 합이 같은 부분집합(DFS)

import sys
#sys.stdin = open("input.txt", "rt")

def DFS(L, sum):
    if sum>total//2: #시간 복잡도를 줄이기 위한 추가 코드
        return #함수 중단
    if L==n:
        if sum==(total-sum):#total이 홀수인경우이면 sum=total//2인 경우가 있어서
            #이부분을 sum==total//2로 해서는 안된다.
            print("YES")
            sys.exit(0) #프로그램 완전 종료
    else:
        DFS(L+1, sum+a[L]) #더해주는 경우
        DFS(L+1, sum) #안 더해주는 경우

if __name__="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
    print("NO") #재귀가 돌고 끝나버린 경우


'''
#sys.exit(0)을 못쓰는 경우

def DFS(L, subTotal):
    global switch
    if switch: return
    if L == n:
        if subTotal == (total_sum - subTotal):
            print("Yes")
            switch = 1
    else:
        DFS(L+1, subTotal + num_lst[L])
        DFS(L+1, subTotal)

if __name__ == '__main__':
    switch = 0
    n = int(input()) # 원소 개수
    num_lst = list(map(int, input().split()))
    total_sum = sum(num_lst)
    DFS(0, 0)
    if switch==0: print("NO")
'''


'''
#나의 풀이

def DFS(v):
    if v==n:
        if sum(b)==c/2:
            print("YES")
            exit()          
    else:
        b.append(a[v])
        DFS(v+1)
        b.remove(a[v])
        DFS(v+1)
        
if __name__ == "__main__":
    n=int(input())
    a=list(map(int, input().split()))
    c=sum(a)
    b=[]
    DFS(0)
    print("NO")
'''

    

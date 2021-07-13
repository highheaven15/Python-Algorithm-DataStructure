#09. 수열 추측하기(순열, 파스칼 응용)

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0) #찾게 되면 그것이 가장 앞에 오는것이 자동으로 되므로 프로그램 종료
    else:
        for i in range(1, n+1): #순열 만들기
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0


if __name__=="__main__":
    n, f = map(int, input().split())
    p=[0]*n #순열이 들어갈 자리
    b=[1]*n #이항 계수가 들어갈 자리
    ch=[0]*(n+1)

    for i in range(1, n):
        b[i]=b[i-1]*(n-i)//i #/i로 나누면 불필요한 소수점이 생기므로..
    DFS(0, 0)
        #for x in b:
        #    print(x, end=' ')

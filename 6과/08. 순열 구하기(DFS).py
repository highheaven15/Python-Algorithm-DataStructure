#08. 순열 구하기(DFS)

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for j in range(1, n+1): #가지 뻗기
            if ch[j]==0:
                ch[j]=1 #호출하기 전 작업, 체크 해주고
                res[L]=j #호출하기 전 작업
                DFS(L+1)
                ch[j]=0 #호출끝나고 후 작업, 체크 풀어주고 


    
if __name__=="__main__":
    n, m = map(int, input().split())
    res=[0]*m
    ch=[0]*(n+1) #체크 변수
    cnt=0
    DFS(0)
    print(cnt)

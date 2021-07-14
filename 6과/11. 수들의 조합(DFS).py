#11. 수들의 조합(DFS)

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, s, sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for j in range(s, n):
            DFS(L+1,j+1, sum+a[j])
                
if __name__=="__main__":
    n, k = map(int, input().split()) #n=5, k=3
    a=list(map(int, input().split())) #2 4 5 8 12
    m = int(input()) #6
    cnt=0
    DFS(0, 0, 0)
    print(cnt)

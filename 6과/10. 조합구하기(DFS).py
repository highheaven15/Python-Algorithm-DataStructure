#10. 조합구하기(DFS)

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, s):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        cnt+=1
        print()
    else:
        for j in range(s, n+1):
            res[L]=j
            DFS(L+1,j+1) 
                
if __name__=="__main__":
    n, m = map(int, input().split()) #n=4, m=2
    cnt=0
    res=[0]*m
    DFS(0, 1)
    print(cnt)

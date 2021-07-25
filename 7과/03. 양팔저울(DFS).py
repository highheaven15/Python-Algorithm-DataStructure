#03. 양팔저울(DFS)

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:#양수만 체크해주면 된다.
            res.add(sum)
    else:
        DFS(L+1, sum+G[L]) #추를 왼쪽에 놓는다!
        DFS(L+1, sum-G[L]) #추를 오른쪽에 놓는다!
        DFS(L+1, sum) #추를 사용하지 않는다.


if __name__=="__main__":
    n=int(input()) #추의 개수
    G=list(map(int, input().split())) #추의 무게
    s=sum(G)
    res=set() #집합 자료구조형, 중복을 제거
    DFS(0, 0)
    print(s-len(res))

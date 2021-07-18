#02. 네트워크 선 자르기(Top-Down : 재귀, 메모리제이션)

#다이나믹 문제를 푸는데 Top-Down의 방법도 있다 정도입니다.
#다이나믹 문제 거의 대부분은 Bottom-Up방식으로 해결하는게 정석입니다.

#메모를 해놓고 불필요한 재귀호출을 방지한다.

import sys
sys.stdin=open("input.txt", 'r')

def DFS(len):
    if dy[len]>0: #메모리안에 값이 이미 들어가있다는 의미
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2) #메모리제이션
        return dy[len]


if __name__=="__main__":
    n=int(input())
    dy=[0]*(n+1)
    print(DFS(n))

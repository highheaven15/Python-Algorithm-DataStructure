#03. 도전과제 - 계단오르기, 돌다리 건너기
#(네트워크 선자르기와 동일)

import sys
sys.stdin = open("input.txt", "rt")

#Bottom-Up

n=int(input())
dy=[0]*(n+1)
dy[1]=1 #직관적으로 알수있는 것들은 초기값 세팅
dy[2]=2
for i in range(3, n+1):
    dy[i]=dy[i-2]+dy[i-1]

print(dy[n])

#Top-Down

def DFS(len):
    if dy[len]>0: #메모리안에 값이 이미 들어가있다는 의미
        return dy[len]

    if len==1 or len==2:
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2) #메모리제이션
        return dy[len]

if __name__=="__main__":
    n=int(input()
    dy=[0]*(n+1)
    print(DFS(n))

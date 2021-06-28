#01. 재귀함수를 이용한 이진수 출력

import sys
sys.stdin=open("input.txt", "r")

def DFS(x):
    if x==0:
        return #함수를 종료하겠다는 의미
    else:
        DFS(x//2)
        print(x%2, end='')
        

if __name__=="__main__":
    n=int(input())
    DFS(n)

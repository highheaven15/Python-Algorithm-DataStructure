#[선수지식] 재귀함수와 스택

import sys
sys.stdin = open("input.txt", "rt")
#재귀함수 =자기자신을 호출하는 함수, 스택을 이용
#반복문의 효과를 내는것이 재귀함수, 단순 반복문의 대체제
#for문의 중첩으로 하기에는 코드 유연성이 떨어지는것을 재귀함수 사용시 유리

def DFS(x): #지역변수 x로 받음 #1 2 3 로 출력
    if x>0:
        DFS(x-1)
        print(x, end=' ')
        


if __name__=="__main__": #메인 함수 선언, 스크립트가 실행되면 여기부터 실행
    n=int(input())
    DFS(n) #Depth First Search 깊이우선탐색




'''
def DFS(x): #3 2 1 로 출력
    if x>0:
        print(x, end=' ')
        DFS(x-1)
'''

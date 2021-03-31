#07. 교육과정 설계

import sys
sys.stdin=open("input.txt", "rt")

from collections import deque

need=input() #CBA
n=int(input()) #플랜 개수 #3

for i in range(n):  #n바퀴
    plan=input()
    dq=deque(need) #플랜읽을때마다 dq초기화 #CBDAGE
    for x in plan:
        if x in dq: #x가 dq안에 있는지?
            if x!=dq.popleft(): #필수과목의 맨 앞과 일치하지 않으면 순서에 어긋나
                    print("#%d NO" %(i+1))
                    break
    else: #순서가 통과함
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else: #현수가 필수과목을 다 안햇다는 의미
            print("#%d NO" %(i+1))

#다른풀이1-need안에 있는 문자만 모아서 need와 같은지 비교

import sys
sys.stdin=open("input.txt", "rt")

from collections import deque

need=input() #CBA
n=int(input()) #플랜 개수 #3

res=""

for i in range(n):
    plan=input()
    dq=deque(plan)
    while dq: #dq가 빌때까지 계속 반복
        a=dq.leftpop() #C
        if a in need:
            res +=a
    if res==need:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
    res ="" #for문 한번돈후 초기화

#다른풀이2-need안에 있는 문자가 need와 순서가 같은지 비교, deque 안씀

import sys
sys.stdin = open("input.txt", "rt")

need=input() #CBA
n=int(input())

for i in range(n):
    plan=input() #CBDAGE
    s=0
    for x in plan: #C
        if x in need:
            s+=1
            if x!=req[s-1]:
                print("#%d NO" %(i+1))
                break
    else:
        if s=len(need):
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

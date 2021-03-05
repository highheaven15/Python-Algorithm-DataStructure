#08. 침몰하는 타이타닉

import sys
#sys.stdin=open("input.txt", "rt")

N, M= map(int, input().split()) #20명, 최대 120KG
weight=list(map(int, input().split()))

weight.sort() #[21, 24, 25, 30, 36, 55, 55, 67, 68, 72, 75, 80, 81, 83, 85, 95, 105, 111, 115, 119]

cnt=0 #구명보트의 개수

#강의 풀이-list사용

while weight: #weight이 비어있지 않으면 True, 비어있으면 False
    if len(weight)==1:
        cnt+=1
        break
    if weight[0]+weight[-1] > M:
        weight.pop()
        cnt+=1
    else:
        weight.pop(0)
        weight.pop()
        cnt+=1
        
print(cnt)

#강의 풀이-deque사용
import sys
from collections import deque
#sys.stdin=open("input.txt", "rt")

N, M= map(int, input().split()) 
weight=list(map(int, input().split()))

weight.sort()
weight=deque(weight) #weight라는 리스트가 데크가 된다.
cnt=0 #구명보트의 개수

while weight: #weight이 비어있지 않으면 True, 비어있으면 False
    if len(weight)==1:
        cnt+=1
        break
    if weight[0]+weight[-1] > M:
        weight.pop()
        cnt+=1
    else:
        weight.popleft() #여기가 다름, 왼쪽자료를 꺼낼때 popleft()이
        weight.pop()
        cnt+=1
        
print(cnt)

#나의 풀이

while True:
    if len(weight)==1:
        weight.pop()
        cnt+=1
        break
    if weight[0]+weight[-1] > M:
        weight.pop()
        cnt+=1
    else:
        weight.pop(0)
        weight.pop()
        cnt+=1
    if len(weight)==0:
        break    
    
print(cnt)

#인프런 다른 풀이

import sys
sys.stdin=open("input.txt", "rt")

N, M= map(int, input().split()) #20명, 최대 120KG
weight=list(map(int, input().split()))

weight.sort() #[21, 24, 25, 30, 36, 55, 55, 67, 68, 72, 75, 80, 81, 83, 85, 95, 105, 111, 115, 119]

cnt=0

lt=0
rt=n-1

while lt<=rt:
    if weight[lt]+weight[rt]<=M:
        cnt+=1
        lt+=1
        rt-=1
    else:
        cnt+=1
        rt-=1
print(cnt)
            










#07. 창고정리(그리디)

import sys
sys.stdin=open("input.txt", "rt")

#나의 길이

l=int(input()) #창고의 가로 길이
numbers=list(map(int,input().split())) #l개의 자연수-높이
m=int(input()) #높이 조정 횟수

for i in range(m): #m회 조정될꺼다
    numbers.sort(reverse=True)
    numbers[0]-=1
    numbers[-1]+=1

numbers.sort(reverse=True)
print(numbers[0]-numbers[-1])


#강의 풀이

l=int(input())
numbers=list(map(int,input().split()))
m=int(input())

numbers.sort()
for _ in range(m):
    numbers[0]+=1
    numbers[l-1]-=1
    numbers.sort()

print(numbers[l-1]-numbers[0])

#강의 댓글중..시간복잡도측면에서 for문에 sort()를 매번 하지 않으려면?

#입력중 창고 가로의 길이인 L값과 높이 조정 횟수인 M값이 커진다면
#매번 sort하는 코드로는 시간초과가 날겁니다.
#이때는 리스트를 이용한 해쉬방법을 사용하면 좋습니다.
L=int(input())
arr=list(map(int, input().split()))
m=int(input())

cnt=[0]*101
maxH=float('-inf')
minH=float('inf')

for x in arr:
    cnt[x]+=1
    if x>maxH:
        maxH=x
    if x<minH:
        minH=x

for _ in range(m):
    if cnt[maxH]==1:
        cnt[maxH]-=1
        maxH-=1
        cnt[maxH]+=1
    else:
        cnt[maxH]-=1
        cnt[maxH-1]+=1

    if cnt[minH]==1:
        cnt[minH]-=1
        minH+=1
        cnt[minH]+=1
    else:
        cnt[minH]-=1
        cnt[minH+1]+=1

print(maxH-minH)

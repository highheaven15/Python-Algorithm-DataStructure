#06. 씨름선수(그리디)

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

member=[]
for i in range(n):
    h, w =map(int, input().split())
    member.append((h, w))#튜플 삽입

member.sort(reverse=True) #첫번째자료에 의해 내림차순 정렬 

#나의 풀이 member.sort(key=lambda x: x[0],reverse =True)


largest=0
cnt=0
for h, w in member:
    if w>largest: #최대값 갱신
        cnt+=1
        largest=w
print(cnt)

#04. 두 리스트 합치기

#강의 풀이
import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
a=list(map(int, input().split()))

m=int(input())
b=list(map(int, input().split()))

p1=p2=0
c=[]

while p1<n and p2<m: #p1<n 이나  p2<m 둘중 하나가 끝나야 중지
                     #주의 : while p1<n or p2<m:였으면 둘 중하나가 끝나도 안끝나, 둘다 끝나야지 중지
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1 + = 1
    else:
        c.append(b[p2])
        p2 + = 1
#이제 언젠가 둘 중 하나가 끝날것이다.

if p1<n: #p1이 n까지 못가고 남은것, 즉 p2쪽이 종료
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]

for x in c:
    print(x, end=' ')


#나의 풀이-파이썬의 리스트 합을 이용한 풀이
n=int(input())
a=[0]*n

a=list(map(int, input().split()))
#print(a)

m=int(input())
b=[0]*m

b=list(map(int, input().split()))
#print(b)

c=a+b
c=sorted(c)

for x in c:
    print(x, end=" ")

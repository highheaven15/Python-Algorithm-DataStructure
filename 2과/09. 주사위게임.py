#09. 주사위게임

import sys
sys.stdin=open("input.txt", "rt")

#강의 풀이

n=int(input())
res=0

for i in range(n):
    tmp=input().split() #문자화된 숫자
    tmp.sort() #오름차순 정렬
    a, b, c=map(int, tmp)

    #if~elif~elif~else문을 쓸때는 가장좋은 것을 if문에 쓰기
    if a==b and b==c: #가장 좋은 거 3개가 같은 경우
        money=10000+(a*1000)
    elif a==b or a==c: #두번째는 2개가 같은 경우
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100 #정렬되있어서 c가 가장 작다.

    if money>res:
        res=money
print(res)

#나의 첫번째 시도
'''
n=int(input())
emp=[]
for i in range(n):
    a=list(map(int,input().split()))
    
    if a[0]==a[1] and a[1]==a[2]:
        emp.append(a[0]*1000+10000)
    if a[0]==a[1] and a[0]!=a[2] and a[1]!=a[2]:
        emp.append(a[0]*100+1000)     
    if a[0]!=a[1] and a[0]==a[2] and a[1]!=a[2]:
        emp.append(a[0]*100+1000)
    if a[0]!=a[1] and a[0]!=a[2] and a[1]==a[2]:
        emp.append(a[1]*100+1000)
    if a[0]!=a[1] and a[0]!=a[2] and a[1]!=a[2]:
        emp.append(max(a)*100)

print(max(emp))
'''
#나의 두번째 시도
'''
n=int(input())
emp=[]
for i in range(n):
    a=list(map(int,input().split()))
    
    if a[0]==a[1] and a[1]==a[2]:
        emp.append(a[0]*1000+10000)
    elif a[0]==a[1] or a[0]==a[2]:
        emp.append(a[0]*100+1000)     
    elif a[1]==a[2]:
        emp.append(a[1]*100+1000)
    else:
        emp.append(max(a)*100)

print(max(emp))
'''

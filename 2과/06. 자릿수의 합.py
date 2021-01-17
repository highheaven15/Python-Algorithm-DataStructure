#06. 자릿수의 합
import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
a=list(map(int, input().split()))

#몫과 나머지를 이용한 방법

def digit_sum(x):
    sum=0
    while x>0:
        sum += x % 10
        x = x//10 #10으로 나눈 몫
    return sum

max = -2147000000 #정수형은 4바이트
for x in a: #a의 리스트를 하나하나 접근
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)

#string 처리를 이용한 방법
def digit_sum(x):
    sum=0
    for i in str(x): #x의 문자하나하나를 i가 접근
        print(i, end=' ')
        sum += int(i)
    return sum

#나의 풀이 - for x in a를 사용하지 않았다.

def digit_sum(x):
    sum=0
    while(True):
        
        k = x % 10
        x = (int)(x/10)
        sum += k
        
        if x==0:
            break
    return sum

list=[]

for i in range(n):
    list.append(digit_sum(a[i]))

#print(list)

max= -147200000000
for i in range(n):
    if list[i] >max:
        max=list[i]

c=[]

for i in range(n):
    if list[i]==max:
        c.append(a[i])


print(c)

mont=-1472000000

for i in range(len(c)):
    if mont < c[i]:
        mont = c[i]

print(mont)      

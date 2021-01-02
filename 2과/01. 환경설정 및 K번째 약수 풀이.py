1. 환경설정 및 K번째 약수 풀이

import sys
#sys.stdin=open("input.txt", "rt")

n, k =map(int, input().split()) #띄어쓰기 구분된 입력을 불러왔다는 의미

#나의 풀이-리스트를 이용하는 방식

a=[]

for i in range(1, n+1):
    if n % i ==0:
        a.append(i)

if len(a)>=k:
   print(a[k-1])
else :
   print(-1)
   

# 강의 풀이-cnt에 누적하는 방식

'''
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt +=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)    
''' 

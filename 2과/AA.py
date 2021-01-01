import sys
#sys.stdin=open("input.txt", "rt")

n, k =map(int, input().split()) #띄어쓰기 구분된 입력을 불러왔다는 의미

a=[]

for i in range(1, n+1):
    if n % i ==0:
        a.append(i)

if len(a)>=k:
   print(a[k-1])
else :
   print(-1)

#10. 역수열(그리디)

import sys
sys.stdin=open("input.txt", "rt")

#강의 풀이
n=int(input())
a=list(map(int, input().split())) #역수열

seq=[0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0: #자기앞의 빈공간을 다 확보했다는 의미 and
                                  #넣을 자리가 차있을수도있으니 차있으면 다음으로 이동
            seq[j]=i+1
            break #안쪽 for문 탈출
        elif seq[j]==0:
            a[i]-=1
for x in seq:
    print(x, end=' ') 


#코드 구현상으로 a[i]값은 i+1이라는 값의 앞에 i+1보다 큰 숫자가 존재해야 하는 개수입니다.
#빈 공간이 큰 숫자가 들어가는 위치이고 발견될 때 마다 a[i]값을 하나씩 줄여
#a[i]값이 0이 됬다면 자리를 모두 확보했으니 그 다음 빈 공간에 i+1값을 넣어주는 것입니다.

#나의 풀이

N = int(input()) #자연수의 개수
numbers=list(map(int, input().split())) #역수열 [5, 3, 4, 0, 2, 1, 1, 0]

basket=[0]*N #[0, 0, 0, 0, 0, 0, 0, 0]
cnt=0
#print(basket)

for index, x in enumerate(numbers): #index : 2, x=4 
    for a, b in enumerate(basket):
        if b==0:
            cnt+=1
            if cnt>x:
                basket[a]=index+1
                #print(basket)
                cnt=0
                break #안쪽 반복문을 탈출한다.

for k in basket:
    print(k, end=' ')

#다른 풀이1
N = int(input()) #8
                                   # 0  1  2  3  4  5  6  7
a = list(map(int,input().split())) #[5, 3, 4, 0, 2, 1, 1, 0]

seq = []

i = N #8

while i>0:

    seq.insert(a[i-1],i)
    print(seq)
    i -= 1



for x in seq:

    print(x,end=' ')

#다른 풀이2
    
n=int(input())

a=list(map(int,input().split()))

b=[n]

k=n

for i in range(-2,-n-1,-1):
    print(i)

    k-=1

    b.insert(a[i],k)
    print(b)


#print(b)

#다른 풀이3
n = int(input())#8

a =list(map(int,input().split())) #[5, 3, 4, 0, 2, 1, 1, 0]
         
a = a[::-1] #[0, 1, 1, 2, 0, 4, 3, 5]

ans=[]

for x in a:

        ans.insert(x,n)
        print(ans)
        n -=1

#print(ans)

#역수열은 1부터 처리해도 되고, N부터 처리해도 됩니다.원리는 같습니다.
#N부터 처리한다는 것은 ans에 이미 들어가 있는 숫자는 현재 처리하려는 숫자보다
#모두 크다는 것이므로 현재 처리하려는 숫자가 x번 index로 insert되면
#자기 앞에 무조건 큰 숫자가 x개 생기고 현재 숫자 다음에 처리되는 숫자들은
#자기보다 작기때분에 어디에 insert 되도 상관없습니다.




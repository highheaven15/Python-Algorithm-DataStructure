#08. 곶감(모래시계)
import sys
sys.stdin=open("input.txt", "rt")

n =int(input())

a=[list(map(int, input().split())) for _ in range(n)]

#강의 풀이 -pop, append 이용

m=int(input())

for _ in range(m):
    rownum, vector, rotnum = map(int,input().split())
    
    if vector==0:
        for _ in range(rotnum):
            a[rownum-1].append(a[rownum-1].pop(0))        
    else:
        for _ in range(rotnum):
            a[rownum-1].insert(0, a[rownum-1].pop())

start=0
end=n

hap=0

for i in range(n):
    for j in range(start,end):
        hap += a[i][j]
    if i <n//2:
        start += 1
        end -= 1
    else:
        start -=1
        end += 1
        
print(hap)

#나의 풀이

m=int(input())

for _ in range(m):
    rownum=vector=rotnum=0
    
    rownum, vector, rotnum = map(int,input().split())
    rotnum =rotnum % n #rotnum이 n보다 커서 1바퀴이상 도는경우 대비
    
    if vector==0:
        a[rownum-1]=a[rownum-1][rotnum:n]+a[rownum-1][:rotnum]
        
    else:
        a[rownum-1]=a[rownum-1][n-rotnum:]+a[rownum-1][:n-rotnum]


start=0
end=n

hap=0

for i in range(n):
    for j in range(start,end):
        hap += a[i][j]
    if i <n//2:
        start += 1
        end -= 1
    else:
        start -=1
        end += 1
        
print(hap)

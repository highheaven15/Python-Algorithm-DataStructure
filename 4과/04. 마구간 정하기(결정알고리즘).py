#04. 마구간 정하기(결정알고리즘)

import sys
#sys.stdin=open("input.txt", "rt")

def Count(len):
     cnt=1 #첫번째 마구간에 첫번째 말 배치
     endpoint=Line[0] #마지막 말의 위치-첫번째 말 배치 상태

     for i in range(1, n):
         if Line[i]-endpoint>=len:#배치가능, 현재말의 위치-마지막 말의 위치
             cnt+=1
             endpoint=Line[i]
     return cnt
    
n, c=map(int, input().split())
Line=[]

for _ in range(n):
    tmp=int(input())
    Line.append(tmp)

Line.sort()
lt=1 #최소 두 말 사이의 거리
rt=max(Line) #강의 풀이: 정렬된 상태이므로 Line[n-1]로 해도 된다.

while lt<=rt:
    mid=(lt+rt)//2

    if(Count(mid))>=c: #답이 될수가 있다.
        res=mid
        lt=mid+1 #작은 값들을 제거
    else:
        rt=mid-1 #큰 값들을 제거
        
print(res)
            

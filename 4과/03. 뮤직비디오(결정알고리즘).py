#03. 뮤직비디오(결정알고리즘)

#강의 풀이

import sys
#sys.stdin=open("input.txt", "rt")

def count(Capacity):
    cnt=1
    sum=0 #Music을 하나하나 더해간다
    
    for x in Music:
        if sum+x >Capacity:
            cnt+=1 #새로운 dvd추가
            sum=x #새로운 dvd의 첫 곡은 x로 설정
        else:
            sum+=x
    return cnt

m, n =map(int, input().split())
Music =list(map(int, input().split()))


lt=1
rt=sum(Music) #리스트의 합
res=1

while lt<=rt:
    mid=(lt+rt)//2 #mid가 DVD의 한장의 크기가 된다.
   
    if count(mid)<=n:
        res=mid
        rt=mid-1
    else: #용량이 작다는 의미
        lt=mid+1
        
print(res)


#나의 풀이
import sys
#sys.stdin=open("input.txt", "rt")

def count(Capacity):
    cnt=1
    sum=0 #Music을 하나하나 더해간다
    
    for x in Music:
        sum +=x
        if sum>Capacity:
            cnt+=1 #새로운 dvd추가
            sum=x #새로운 dvd의 첫 곡은 x로 설정
    return cnt

m, n =map(int, input().split())
Music =list(map(int, input().split()))


lt=1
rt=sum(Music) #리스트의 합
res=1

while lt<=rt:
    mid=(lt+rt)//2 #mid가 DVD의 한장의 크기가 된다.
   
    if count(mid)<=n:
        res=mid
        rt=mid-1
    else: #용량이 작다는 의미
        lt=mid+1
        
print(res)

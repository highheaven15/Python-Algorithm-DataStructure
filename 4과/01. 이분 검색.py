#01. 이분 검색

import sys
#sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
a=list(map(int, input().split()))
a.sort() #정렬 필요

lt=0
rt=n-1 #a의 0인덱스부터 값이 들어갔으므로
while lt<=rt: #lt>rt가 되면 탐색이 다 끝난것
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1) #몇번째 값인지 출력
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1
        
     

 

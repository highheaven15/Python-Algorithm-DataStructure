#05. 수들의 합

n, m = map(int,input().split())

a=list(map(int,input().split()))

#강의 풀이
lt=0
rt=1
tot=a[0]
cnt=0

whilt True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot -=a[lt]
        lt+=1
    else:


#나의 풀이- 좋은 시도였으나 2중 for문의 시간복잡도가 너무 컸다.
sum=0

for i in range(n):
    res=0
    if a[i] >m:
        continue
    
    elif a[i]==m:
        sum+=1
   
    else:
        res+=a[i]
        for j in range(i+1,n):
            res += a[j]
            if res==m:
                sum+=1
                
print(sum)


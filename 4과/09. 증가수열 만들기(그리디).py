#09. 증가수열 만들기(그리디)

import sys
#sys.stdin=open("input.txt", "rt")

N = int(input()) #자연수의 개수
a=list(map(int, input().split())) #수열
#강의 풀이
lt=0
rt=n-1
last=0
res="" #문자열
tmp=[]

while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[lt], 'R'))
    tmp.sort() #첫자료값에 의해 정렬

    if len(tmp)==0:
        break
    else:
        res+=tmp[0][1] #tmp의 맨 앞자료의 'L' or 'R'이라는 의미
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
    
print(len(res))
print(res)   

#나의 풀이
stnum=0
str=''
'''
생각해보니 딱히 필요없는 부분!
if numbers[0]<numbers[-1]:
    stnum=numbers[0]
    numbers.pop(0)
    str+='L'
else:
    stnum=numbers[-1]
    numbers.pop()
    str+='R'
'''
while True:
    if stnum<numbers[0]<numbers[-1]:
        stnum=numbers[0]
        numbers.pop(0)
        str+='L'
    elif stnum<numbers[-1]<numbers[0]:
        stnum=numbers[-1]
        numbers.pop()
        str+='R'
    elif numbers[0]<stnum<numbers[-1]:
        stnum=numbers[-1]
        numbers.pop()
        str+='R'
    elif numbers[-1]<stnum<numbers[0]:
        stnum=numbers[0]
        numbers.pop(0)
        str+='L'
    elif numbers[0]<numbers[-1]<stnum:
        break
    elif numbers[-1]<numbers[0]<stnum:
        break
    else: #자료가 1개 남아서 numbers[0], numbers[-1] 의 비교가 불가능한 경우
        break
print(len(str))
print(str)
    

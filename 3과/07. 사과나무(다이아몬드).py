#07. 사과나무(다이아몬드)

import sys
sys.stdin=open("input.txt", "rt")

n =int(input())

a=[list(map(int, input().split())) for _ in range(n)]

#나의 풀이-규칙을 찾아서 i, j설정하려했으나 구간은 설정하기 힘들듯

t=0
hap=0
for i in range(n):
    hap += sum(a[i][(n//2-t):(n//2+t+1)])

    if i<n//2:
        t +=1
    else:
        t -=1

print(hap)
        
#2차원 리스트의 슬라이싱
#list[행번호][슬라이싱할 열 구간]

#강의 풀이 -start, end 이용
start=end=n//2
hap=0

for i in range(n):
    for j in range(start, end+1):
        hap+=a[i][j]
    if i<n//2:
        start-=1
        end+=1
    else:
        start+=1
        end-=1
        
print(hap)


#13. 수들의 조합-라이브러리를 이용한 순열(itertools)

import sys
import itertools as it

#조건에 맞는 원소들로 순열, 조합을 만드는 경우에는 라이브러리 무용지물
#DFS로 하는 방법이 정석

sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a=list(map(int, input().split()))
m=int(input())

cnt=0

for tmp in it.combinations(a, k): #a라는 리스트에서 k개만 뽑기
    #print(tmp)
    if sum(tmp)%m==0:
        cnt+=1
print(cnt)


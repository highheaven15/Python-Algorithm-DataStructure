#12. 수열 추측하기-라이브러리를 이용한 순열(itertools)

import sys
import itertools as it

#조건에 맞는 원소들로 순열, 조합을 만드는 경우에는 라이브러리 무용지물
#DFS로 하는 방법이 정석

sys.stdin = open("input.txt", "rt")

n, f = map(int, input().split())

b=[1]*n
cnt=0
for i in range(1, n):
    b[i]=b[i-1]*(n-i)//i

a=list(range(1, n+1)) #[1, 2, 3, 4]

for tmp in it.permutations(a): #---------a 반복문
    sum=0
    for L, x in enumerate(tmp): #L은 인덱스 번호, x는 그 튜플 값
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break  #------a 반복문을 break 하게 된다.
'''
for tmp in it.permutations(a): #a에 있는 요소를 순열로 구해서 tuple형태로 tmp저장
    print(tmp) #4!=24가지가 나옴
    cnt+=1
print(cnt) #24

(1, 2, 3, 4)
(1, 2, 4, 3)
(1, 3, 2, 4)

for tmp in it.permutations(a,3): #3가지를 뽑는 경우 4C3
    print(tmp)

(1, 2, 3)
(1, 2, 4)
(1, 3, 2)
'''

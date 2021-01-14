#04. 대표값

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

# ave=round(sum(a)/len(a)) #평균

ave =sum(a)/len(a)
ave =ave+0.5
ave =int(ave)
print(ave)

min=2147000000 #큰숫자의 예시, 정수형크기의 가장 큰 값 

for idx, x in enumerate(a): #학생번호, 학생 값 모두 이용하기위하여
    tmp = abs(x-ave) #tmp는 거리 변수
    if tmp<min:
        min=tmp
        score=x
        res=idx+1 #0번 인덱스=>1번 학생이므로

    elif tmp==min:
        if x>score:
            score=x
            res=idx+1

print(ave, res)

#파이썬 알고리즘-대표값 문제 수정

#round_half_up이 아닌 round_half_even 방식을 택한다.
a=4.500
print(round(a)) #4, 딱 중앙이면 짝수쪽으로 근사한다.

b=5.500
print(round(b)) #6

a=66.5
a=a+0.5
a=int(a)
print(a) #67

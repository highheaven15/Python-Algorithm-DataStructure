#05. 회의실 배정(그리디)

#문제를 풀어나가는 과정, 단계에 있어 그 단계에서 가장 좋은 것을 선택
#보통의 그리디 문제->정렬!과 동반

#끝나는 시간이 빠른게 중요하다=>끝나는 시간 기준 정렬

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

meeting=[]
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((s, e))
    
#meeting.sort() start값으로 정렬하고 start가 같으면 end로 정렬
meeting.sort(key=lambda x: (x[1], x[0]))
#lambda : 익명함수 #end에 의해 정렬된다.

print(meeting)
et=0
cnt=0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)

#08. 단어찾기

import sys
sys.stdin = open("input.txt", "rt")
#딕셔너리는 리스트와 다르게 문자, 알파벳, 단어도 index값으로 쓰일수있다.
#리스트는 정수(0, 1, 2, 3, 4, -1, -2...)만 index값으로 사용가능

#강의 풀이
n=int(input())
p=dict()

for i in range(n):
    word=input()
    p[word]=1

for i in range(n-1):
    word=input()
    p[word]=0

for key, value in p.items:
    if value==1:
        print(key)
        break

#나의 풀이-집합 자료형 이용, 부분 오류가 있다

n=int(input())
note=set()

for i in range(n):
    a=input()
    note.add(a) #이미 존재하는 단어라면 추가가 되지 않는다.
    #print(note)

for i in range(n-1):
    b=input()
    note.remove(b) #같은 단어가 2번 있으면 2번째 지울때는 오류가 난다.
    #print(note)

for x in note:
    print(x)

#다른 풀이
  
n = int(input())
words = [input() for _ in range(n)] #리스트 형태로 들어감
finds = [input() for _ in range(n-1)]
print(*(set(words) - set(finds)))

#03. 카드 역배치

#나의 풀이
import sys
sys.stdin=open("input.txt", "rt")

list=[]
for i in range(21):
    list.append(i)
#print(list) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(10):
    tmp=input().split()
    start, end = map(int, tmp)
    list[start:end+1]=list[end:start-1:-1]

for x in list:
    if x>0:
        print(x, end=" ")

#강의 풀이
a=list(range(21)) #0~20까지의 숫자가 리스트에 들어간다.


for _ in range(10): #_는 변수 지정없이 그냥 반복문이 돈다
    s, e =map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i] #swap

a.pop(0) #0번 인덱스 뽑아 #a.pop()이면 가장 뒤의 것이 빠짐
for x in a:
    print(x, end=" ")

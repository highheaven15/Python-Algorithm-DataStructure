8. 리스트와 내장함수(1)

#리스트 만들기
c=[]
print(c)

d=list()
print(d)

a=[1,2,3,4,5]
print(a)
print(a[0])

b=list(range(1, 11))
print(b)

c=a+b #리스트 합치기
print(c)


print(a) #[1, 2, 3, 4, 5]

a.append(6) #리스트에 요소 추가
print(a) #[1, 2, 3, 4, 5, 6]

a.insert(3, 7) #리스트의 3번 인덱스 자리에 7을 추가로 삽입하기
print(a) #[1, 2, 3, 7, 4, 5, 6]

a.pop() #리스트 a의 마지막자리 요소를 제거
print(a) #[1, 2, 3, 7, 4, 5]

a.pop(3) #리스트의 3번자리에 있는 요소를 제거
print(a) #[1, 2, 3, 7, 4, 5]


a.remove(4) #리스트에서 4라는 값을 제거해라
print(a) #[1, 2, 3, 5]

print(a.index(5)) #리스트에서 5라는 값의 index를 구해라

a=list(range(1, 11))
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(a)) #55
print(max(a)) #리스트 a에서 가장 큰 값을 출력, 10
print(min(a)) #리스트 a에서 가장 작은 값을 출력, 1

print(min(5, 7)) #min, max는 인자 값들중에서 최소, 최대값을 찾아주는 것


print(a)
import random as r

r.shuffle(a) #리스트 a를 무작위로 섞기
print(a)

a.sort() # 오름차순으로 정렬
print(a)

a.sort(reverse=True) #내림차순으로 정렬
print(a)

a.clear() #리스트의 요소들을 다 지우기
print(a)  # []

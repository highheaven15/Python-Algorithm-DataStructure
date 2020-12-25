12. 람다함수

익명의 함수, 람다 표현식이라고도 한다.

def plus_one(x):
    return x+1

print(plus_one(1))

plus_two = lambda x: x+2 #람다 함수는 변수에 할당을 해야함
print(plus_two(4))


a=[1,2,3]
print(list(map(plus_one,a)))
#[2, 3, 4]

#map(함수명, 자료형)=자료형의 인자들을 하나씩 함수적용하기

print(list(map(lambda x : x+1, a)))
#[2, 3, 4]

#람다의 장점은 함수를 만들지 않을수 있다. 함수의 이름 필요없고
#내장함수의 인자로 사용할때 편리하다.

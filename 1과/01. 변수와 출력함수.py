1. 변수와 출력함수

#변수명 정하기

1. 영문과 숫자, _로 이루어진다.

2. 대소문자를 구분한다.

3. 문자나, _로 시작한다. 2b=4 불가능(숫자로 시작하는 것 불가능)

4. 특수문자를 사용하면 안된다.(&,% 등)
    
5. 키워드, 예약어를 사용하면 안된다.(if, for 등)


#여러값 한번에 지정

a, b, c =1, 3, 5

print(a, b, c) #1, 3, 5
 

#값 교환

a, b = 10, 20

print(a,b)

a, b=b, a #파이썬에서는 가능

print(b,a) #20, 10


#변수 타입

a=12345

print(type(a)) # <class 'int'>


b=123.455

print(type(b)) # <class 'float'>


c=123.333333333333333333 #너무 큰 수를 입력하면 중간에 짤린다. 실수형은 최대 8byte


d='student'

print(type(d)) # <class 'str'>


#출력방식

print("number")

a, b, c=1, 2, 3

print(a, b, c) #기본은 띄어쓰기 한자리를 한다.

print("number", a, b, c)
 

print(a, b, c, sep='') #abc 아무것도 안넣으면 붙여서 나옴

print(a, b, c, sep=',') #a,b,c

print(a, b, c, sep='\n') #한줄 엔터로 구분됨

print(a) #출력 후 자동 엔터
print(b)
print(c)

#1
#2
#3

print(a, end=' ') #줄바꿈을 안해주고 옆으로 띄어쓰기 한칸

print(b, end=' ')

print(c)

#1 2 3

2. 변수입력과 연산자

a=input()
print(a)

a=input("숫자를 입력하세요 : ")
print(a)


#입력하면서 띄어쓰기로 구분하기

a, b = input("숫자를 입력하세요 : ").split() #2 3 입력
print(a, b)
print(a+b) #문자끼리 연결하게 된다..23


print(type(a)) #<class 'str'>
c =a+b
print(type(c)) #<class 'str'>
print(c)

#입력값을 정수로 바꾸기

a,b =input("숫자를 입력하세요 : ").split()

a=int(a)
b=int(b)
print(a+b)


#입력값을 정수로 바꾸기-map 내장함수이용

a, b =map(int, input("숫자를 입력하세요 : ").split())
print(a+b) #합
print(a-b) #차
print(a*b) #곱셈
print(a/b) #나눗셈
print(a//b) #나눗셈의 몫
print(a%b) #나눗셈의 나머지
print(a**b) #a의 b거듭제곱


#실수형과 정수형 변수 더하기-형이 다른 연산을 하면 결과는 넓은 범위로 나온다
a=4.3
b=5
c=a+b
print(type(c)) # <class 'float'>
#실수형의 범위가 정수형의 범위를 포함하므로 c는 실수형

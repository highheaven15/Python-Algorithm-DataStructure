11. 함수만들기


def add(a, b):
    c= a+ b
    print(c)

add(3,2) #5
add(5,7) #12

def add(a, b):
    c=a+b
    return c #c를 반환시켜

print(add(3,2)) #5

x=add(3,2)
print(x) #역시 5

def add(a,b):
    c=a+b
    d=a-b
    return c, d

print(add(3, 2)) #(5, 1) 튜플로 여러 개 return 가능하다

def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12, 13, 7, 9, 19]

for y in a:
    if isPrime(y): #True면 아래 문장 실행, False면 아래 문장 지나간다.
        print(y, end= ' ')
#13 7 19 

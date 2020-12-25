9. 리스트와 내장함수(2)

a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

#선생님은 이 방법을 선호
for x in a:
    print(x, end=' ')
print()

#홀수만 출력
for x in a:
    if x%2==1:
        print(x, end=' ')
print()

for x in enumerate(a):
    print(x) #enumerate()는 튜플 형태로 출력
'''
(0, 23)
(1, 12)
(2, 36)
(3, 53)
(4, 19)
'''

#튜플-값 변경 불가
b=(1, 2, 3, 4, 5)
print(b[0])
#b[0]=7 #'tuple' object does not support item assignment
print(b[0])

for x in enumerate(a):
    print(x[0], x[1])
print()
'''
0 23
1 12
2 36
3 53
4 19
'''

#선생님은 이 방법을 선호
for index, value in enumerate(a):
    print(index, value)
print()


#all 함수-x값모두가 조건을 만족해야 통과
if all(60>x for x in a):
    print("YES")
else:
    print("NO") #하나라도 참이 아닐때


#any 함수-x값중 하나라도 조건에 만족하면 통과
if any(15>x for x in a):
    print("YES")
else:
    print("NO")

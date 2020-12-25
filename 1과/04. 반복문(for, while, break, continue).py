4. 반복문(for, while, break, continue)

반복문(for, while)


a=range(10)
print(list(a)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a=range(1,11)
print(list(a)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in range(10):
    print("hello")

for i in range(10):
    print(i)


#큰수에서 작은수 갈때는 -얼마 단위로 작아질건지 입력
for i in range(10,0, -1): 
    print(i)


i=1
while i<=10:
    print(i)
    i=i+1


i=10
while i>=1:
    print(i)
    i=i-1


i=1
while True: #항상 참이라는 말
    print(i)
    if i==10:
        break
    i+=1
#10일때 반복문을 멈추게 된다.

#continue

for i in range(1, 11):
    if i%2==0: #i가 짝수면 print하지않고 지나가 버린다..
        continue
    print(i)
#홀수만 출력
    

#for~else구문, for 문이 정상적으로 종료가 되면 else를 하고 for문 중간에 break을 당하면 else를 시행하지 않는다.

# for문 중간에 break을 당해서 else를 시행하지 않는 경우
for i in range(1,11):
    print(i)
    if i==5:
        break
else:
    print(11)


#break를 당하지 않고 for문이 정상적으로 종료가 되는 경우

for i in range(1,11):
    print(i)
    if i>15: #break를 당하지 않고 for문이 정상적으로 종료가 됨
        break
else: 
    print(11) #else가 실행이 된다.

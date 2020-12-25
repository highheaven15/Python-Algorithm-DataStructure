7. 문자열과 내장함수

msg= "It is Time"

print(msg.upper()) #IT IS TIME
print(msg.lower()) #it is time
print(msg) #It is Time, 원본이 바뀌는 건 아니다.

tmp =msg.upper()
print(tmp)
#0123456789
#IT IS TIME

print(tmp.find('T')) #'T'가 가장먼저 나오는 인덱스 넘버 찾기

print(tmp.count('T'))#'T'가 몇번 나오는지

print(tmp[:2]) #0~2-1까지 뽑아낸다.(slicing)

print(tmp[3:5]) #3~4까지 뽑아낸다.

print(len(msg)) #공백을 포함한 msg의 길이 = 10

for i in range(len(msg)):
    print(msg[i], end=' ')

#x가 msg의 문자 하나하나가 된다.
for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper(): #x가 대문자이면 참
        print(x, end=' ') #대문자만 출력
print()

for x in msg:
    if x.islower():
        print(x, end=' ') #소문자만 출력
print()

for x in msg:
    if x.isalpha(): #x가 알파벳인가? 공백이 아니다
        print(x, end='')
print()

#isalpha()는 숫자나 공백이 아닌 알파벳만!!

a= "a1b2c3"

for x in a:
    if x.isalpha():
        print(x, end=' ')
print()


#ord()는 ASCII 코드를 출력, A는 65, Z는 90, a는 97, z는 122, 알파벳 26자

bmp='AZ'
for x in bmp:
    print(ord(x)) #65, 90

cmp='az'
for x in cmp:
    print(ord(x)) #97, 122

tmp=65
print(chr(tmp)) #넘버를 대응되는 아스키문자로 출력, 즉 A출력

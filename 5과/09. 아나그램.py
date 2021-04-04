#09. 아나그램

import sys
sys.stdin = open("input.txt", "rt")

#강의 풀이1(딕셔너리 해쉬) 시간복잡도 O(N)
a=input() #AbaAeCe
b=input()

str1=dict()
str2=dict()

for x in a:
    str1[x]=str1.get(x, 0)+1#'x'라는 key가 존재하면 key, value 쌍을 리턴하고 아니면 0을 리턴

for x in b:
    str2[x]=str2.get(x, 0)+1

for i in str1.keys(): #키값들만 가져오고싶으면
    #print(i) #A, b, a, e, C가 출력됨

    if i in str2.keys(): #str1에 존재하는 key값이 str2에도 존재하면
        if str1[i] != str2[i]: #i가 key인 value의 개수가 동일한지..
            print("NO")
            break
    else: #str1에 존재하는 key값이 str2에도 존재하지않으면
        print("NO")
        break
else: #break에 걸리지 않고 정상적으로 종료 시에
    print("YES")

#다른 풀이2(딕셔너리 해쉬) 마지막에 단순 비교한경우

a=input() #AbaAeCe
b=input()

str1=dict()
str2=dict()

for x in a:
    str1[x]=str1.get(x, 0)+1#'x'라는 key가 존재하면 key, value 쌍을 리턴하고 아니면 0을 리턴

for x in b:
    str2[x]=str2.get(x, 0)+1

if str1==str2:
    print("YES")
else:
    print("NO")


#다른 풀이3(딕셔너리 해쉬)

a=input() #AbaAeCe
b=input()

sH=dict()

for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1


print(sH)
{'A': 0, 'B': 0, 'C': 0, 'D': 0, 'q': 2, 't': 2, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'e': -1, 'a': -1, 'g': 0, 'd': 1, 'X': 0,
 'Y': 0, 'b': 0, 'c': 0, 'f': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
 'n': 0, 'o': 0, 'p': 0, 'r': -1, 's': 0, 'u': 0, 'w': -2, 'x': 0, 'y': 0, 'z': 0}


for x in a:
    if sH.get(x)!=0: #0이 아닌 것이 나오면.. >0으로 해도 무방
        print("NO")
        break
else:
    print("YES")

#다른 풀이4(소트 방식) 시간복잡도 비효율적임 O(N log N)

a=input()
b=input()
print(sorted(a)) #['A', 'A', 'C', 'a', 'b', 'e', 'e']

if sorted(a)==sorted(b):
    print("YES")
else:
    print("NO")


#다른 풀이5-Counter모듈 이용

#collections 모듈의 Counter 클래스는 어떤 문자열이나 숫자 리스트가 주어졌을 때, 
#해당 문자열/리스트에서 어떤 객체가 몇번 등장했는지 알아서 카운트, 딕셔너리로 만들어준다.
#이 때 대/소문자가 구별되며, key 값에는 해당 객체가, value 값에는 해당 객체의 등장 횟수가 들어간다.
from collections import Counter

a=input()
b=input()

#print(Counter(a)) #Counter({'A': 2, 'e': 2, 'b': 1, 'a': 1, 'C': 1})
res=Counter(a)-Counter(b)
    
if len(res)==0:
    print("YES")
else:
    print("NO")


#다른 풀이6- 리스트 해쉬, 아스키 코드 이용

a=input()
b=input()

str1=[0]*52 #알파벳 대소문자 각 26개씩 총 52를 0으로 초기화
str2=[0]*52

#A =65, Z=90, a= 97, z=122

for x in a:
    if x.isupper(): #x가 대문자이면
        str1[ord(x)-65]+=1 #ord는 아스키코드로 바꾸어준다. 인덱스 맞추려고 65를뺌
    else:
        str1[ord(x)-71]+=1 #71을 빼줘야 소문자 a 26번으로 인덱스가 된다.

for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1

#if str1==str2: #두 리스트의 값이 정확히 같으면 참이므로 가능

for i in range(52):
    if str1[i]!=str2[i]: #다른것이 발견되면
        print("NO")
        break
else: #break 안당하고 정상 종료시에는
    print("YES")

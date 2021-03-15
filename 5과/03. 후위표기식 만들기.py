#03. 후위표기식 만들기

#컴퓨터는 중위표기식을 불편해한다.  

import sys
sys.stdin=open("input.txt", "rt")

a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal(): #x가 10진수 숫자, 즉 피 연산자이면 출력
        res+=x
    else: #x는 연산자라는 의미!
        if x=='(': #x가 (이면 무조건 append
            stack.append(x)
        elif x=='*' or x=='/': #x가 *이나 /이면 자기보다 연산순위가 빠른애들만 스택에서 뺀다
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
            #스택이 비어있지 않고 스택 최상단이 *이나 /이면
                res+=stack.pop() #끄집어 내고 출력
            stack.append(x) #+, -, ( 만나면 append
        elif x=='+' or x=='-': #x가 +이나 -이면
            while stack and stack[-1]!='(':
            #스택이 비어있지 않고 스택 최상단이 (전까지만 끄집어 내고 출력
                res+=stack.pop()
            stack.append(x)
        elif x==')': #x가 )이면 스택 최상단이 (전까지만 끄집어 내고 출력
            while stack and stack[-1]!='(':
                res+=stack.pop() 
            stack.pop() #(를 끄집어 없앤다.
#중위식 탐색이 끝나고도 스택에 무언가 남아있을수도있다

while stack: #stack이 비어있을때까지 계속 시행
    res+=stack.pop() #스택의 최상단부터 끄집어 내서 출력
print(res)


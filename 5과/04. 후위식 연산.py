#04. 후위식 연산

import sys
sys.stdin=open("input.txt", "rt")

#강의 풀이
a=input()
stack=[]

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        elif x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
        
print(stack[0])

#나의 풀이
a=input()
stack=[]

for x in a:
    if x.isdecimal():#x가 숫자면 stack 대입
        stack.append(x)
    elif x=='+':
        num2=stack.pop()
        num1=stack.pop()
        num3= int(num1) + int(num2)
        stack.append(num3)
    elif x=='-':
        num2=stack.pop()
        num1=stack.pop()
        num3= int(num1) - int(num2)
        stack.append(num3)
    elif x=='*':
        num2=stack.pop()
        num1=stack.pop()
        num3= int(num1) * int(num2)
        stack.append(num3)
    elif x=='/':
        num2=stack.pop()
        num1=stack.pop()
        num3= int(num1) / int(num2)
        stack.append(num3)
for i in stack:
    print(i)

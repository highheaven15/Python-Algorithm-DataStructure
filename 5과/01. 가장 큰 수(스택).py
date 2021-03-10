#01. 가장 큰 수(스택)

import sys
sys.stdin=open("input.txt", "rt")

num, m=map(int, input().split()) #m은 지워야할 개수

num=list(map(int, str(num)))#str로 만들어서 num을 숫자 하나하나 분리 후 다시 각각 int

#print(num) #[5, 2, 7, 6, 8, 2, 3] <=리스트에 하나하나 숫자로 넣음


stack=[]

for x in num:#stack이 비어있지 않으면 True, 비어있으면 False
    while stack and m>0 and stack[-1]<x:
        #stack이 비어있지 않고 지워야할 개수가 남아있고
        #마지막으로 들어가는 숫자(stack[-1])보다 지금 들어가는 숫자(x)가 크면
        #while 반복문이 계속 유지되면서 숫자를 pop시킨다.
        stack.pop()
        m-=1
    stack.append(x) #while문이 끝나면 x를 삽입

if m!==0: #다 지우지 못하는 경우 고려, 더 지울수있다는 의미
    stack=stack[:-m] #-m 뒤에 부분은 날린다는 의미

#print(stack) #[7, 8, 2, 3]

res=''.join(map(str, stack))
print(res)

#for x in stack:
#    print(x, end='')

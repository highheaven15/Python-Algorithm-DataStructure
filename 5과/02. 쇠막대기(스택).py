#02. 쇠막대기(스택)

import sys
sys.stdin=open("input.txt", "rt")

#강의 풀이
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:#')'이라는 의미
        #여기에 stack.pop()을 해주고 밑에 stack.pop()두개를 지워줘도 된다.
        if s[i-1]=='(': #레이저라는 의미
            stack.pop()
            cnt+=len(stack)
        else: #앞이 ')' 즉 여기는 쇠막대기의 끝이라는 의미
            stack.pop()
            cnt+=1
print(cnt)


#나의 풀이
s=input()
cnt=0 #잘려진 총 조각 수
box=0 #레이저를 맞게 되면 잘라지는 조각의 수

for i in range(len(s)):
    if s[i]=='(' and s[i+1]==')':
        cnt+=box
    elif s[i]=='(' and s[i+1]=='(':
        box+=1
    elif s[i]==')' and s[i-1]==')':
        box-=1
        cnt+=1
        
print(cnt)
 

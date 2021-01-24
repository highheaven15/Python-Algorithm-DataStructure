import sys
sys.stdin=open("input.txt", "rt")
n=int(input())

for i in range(n):
    s=input()
    s=s.upper() #문자열을 대문자로 바꾼다.

    size=len(s) #문자열의 길이

    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1)) #format 형태
            break
    else:
        print("#%d YES" %(i+1))
        
'''
    # 파이썬 스타일로 풀이
    if s==s[::-1]: #뒤에서부터 거꾸로된 문자
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))

'''

#06. 알파코드(DFS)

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end='') #아스키 코드 이용
        print()
        
    else:
        for i in range(1, 27): #1~26까지의 알파벳
            if code[L]==i:
                res[P]=i
                DFS(L+1, P+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                            #10의자리수           1의 자리수
                res[P]=i
                DFS(L+2, P+1)
    
if __name__=="__main__":
    code=list(map(int, input()))
    n=len(code)
    code.insert(n, -1) #이것이 없으면 마지막에 index out of range 에러가 뜬다.
    res=[0]*n #완성된 숫자를 넣음
    cnt=0
    DFS(0, 0)
    print(cnt)

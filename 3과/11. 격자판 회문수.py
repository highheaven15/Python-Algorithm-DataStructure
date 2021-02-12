#11. 격자판 회문수

#강의 풀이
import sys
sys.stdin=open("input.txt", "rt")

board = [list(map(int, input().split())) for _ in range(7)]
cnt=0

for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5] #5칸 슬라이싱
    if tmp == tmp[::-1] #행
        cnt +=1

    for k in range(2): 
        if board[i+k][j] !=board[i+5-k-1][j]: #열
            break
    else:
        cnt +=1

print(cnt)

#나의 풀이

a=[list(map(int, input().split())) for _ in range(7)]
cnt =0

for i in range(7): #행, 열
    start = 0
    for _ in range(3):
        
        if a[i][start]==a[i][start+4] and a[i][start+1]==a[i][start+3]:
            cnt+=1
        if a[start][i]==a[start+4][i] and a[start+1][i]==a[start+3][i]:
            cnt+=1
            
        start+=1
        if start ==3:
            break

print(cnt)

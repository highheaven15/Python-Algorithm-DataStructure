#01. 최대점수 구하기(DFS)

#문제를 풀지 말지 결정만 해주면 된다.

#강의 풀이

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, sum, time):
  global res
  if time>m:
    return     

  if L==n:
    if sum>res:
      res=sum
  else:
    DFS(L+1, sum+pv[L], time+pt[L])
    DFS(L+1, sum, time)


if __name__=="__main__":
    n, m = map(int, input().split()) #문제의 개수 n=5, 제한시간 m=20
    pv=list()
    pt=list()
    for i in range(n):
        a, b=map(int, input().split())
        pv.append(a)
        pt.append(b)
    res=-2187000000
    DFS(0, 0, 0)
    print(res)


#나의 풀이 (변수이름만 바꼈을뿐 정답)

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, timesum, scoresum):
  global maxscore
  if timesum>m:
    return

  if L==n:
    if maxscore<scoresum:
      maxscore=scoresum
  else:
    DFS(L+1, timesum+time[L], scoresum+score[L])
    DFS(L+1, timesum, scoresum)


if __name__=="__main__":
  n, m = map(int, input().split()) #문제의 개수 n=5, 제한시간 m=20
  
  score=[0]*n
  time=[0]*n

  maxscore=-2187000000
  scoresum=0
  timesum=0
  
  for i in range(n):
    score[i], time[i]= map(int, input().split())
  DFS(0, 0, 0)
  print(maxscore)

#조합처럼 푼 다른 사람의 풀이-공책 

import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, total, time):
    global maxscore
    if time>m:
        return
    if total>maxscore:
        maxscore=total

    for i in range(L, n):
        DFS(i+1, total+ques[i][0], time+ques[i][1])

if __name__=="__main__":
    n, m = map(int, input().split())
    ques=[]
    for _ in range(n):
        a, b=map(int, input().split())
        ques.append((a, b))
    maxscore=-2147000000
    DFS(0, 0, 0)
    print(maxscore)


#02. K번째 수

import sys
#sys.stdin=open("input.txt", "rt")

T=int(input())
for t in range(T):
    n, s, e, k = map(int, input().split()) #띄어쓰기 구분된 입력을 불러왔다는 의미
    a = list(map(int, input().split()))
    a = a[s-1:e] # 인덱스 s-1부터 인덱스 e-1까지 출력한다는 의미
    a.sort()
    
    print("#%d %d" %(t+1, a[k-1]))
    
    print("#{} {}".format(t+1, a[k-1]))

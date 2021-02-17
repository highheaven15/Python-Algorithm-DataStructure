#02. 랜선자르기(결정알고리즘)

import sys
sys.stdin=open("input.txt", "rt")

#결정알고리즘에서 이분검색을 사용
#결정 알고리즘으로 풀수있는 문제들은 답을 특정범위안에 있다는 것을 알수있다.
#답을 정해놓고 범위 내의 특정 숫자를 정해놓고 이분검색을 쓴다.
#중앙값을 정해놓고 그 값이 유효한지, 유효한지 않은지 확인하는 함수를 만들어서 확인작업
#답이 되면 범위를 좁힌다. 범위를 좁히면서 더 좋은 값을 구해낸다.

def Count(len): #길이라는 변수를받음
    cnt=0
    for x in Line:
        cnt+= (x//len)
    return cnt


k, n=map(int, input().split())
Line=[]

res=0 #최댓값
largest =0 #가장 긴 랜선

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest=max(largest, tmp) #둘중 큰값을 largest에 갱신

lt=1
rt=largest

while lt<=rt:
    mid=(lt+rt)//2 #mid는 랜선의 길이가 된다.

    if Count(mid)>=n:
        res=mid
        lt=mid+1 #더 긴 좋은 값을 찾아 나선다..
    else: #길어서 답이 안되는것
        rt=mid-1

print(res)

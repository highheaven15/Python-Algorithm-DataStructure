#10. 스토쿠검사

#나의 풀이 - 리스트(1~9)에 담고 지워나가기! 리스트는 없는 원소를 지울때 오류가 난다!

import sys
sys.stdin=open("input.txt", "rt")

a=[list(map(int, input().split())) for _ in range(9)]


#cup = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9):
    cup1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cup2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for j in range(9):
        cup1.remove(a[i][j])
        cup2.remove(a[j][i])
    
    if len(cup1) !=0: or len(cup2) !=0:
        print("NO")
        break
        
for k in range(3):
    for m in range(3):
        cup = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3):
            for j in range(3):
                cup.remove(a[3*k+i][3*m+j])
        if len(cup) !=0:
            print("NO")
            break
        
print("YES")


#강의 풀이 - 리스트에 채워나가기

def check(a): #a는 지역변수
    for i in range(9):
        ch1=[0]*10 #행체크
        ch2=[0]*10 #열체크
        for j in range(9):
            ch1[a[i][j]]=1 #ch에 더해주는것이 아니라 ch1값을 1로 선언
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9: #중복시 1이 아닌 빈 요소가 있으면 합9 불가
            return False
        
    for i in range(3):
        for j in range(3):
            ch3=[0]*10 #그룹체크

            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True


a=[list(map(int, input().split())) for _ in range(9)]

if check(a):
    print("YES")
else:
    print("NO")

#잠깐지식(전역변수와 지역변수)-변수

#전역 변수 : 모든함수가 접근, 변경가능하다. 공용이다.

def DFS1():
    print(cnt) #함수입장에서 지역변수인 cnt가 있나 확인하고 없으면
      #5       #전역변수가 있나 확인 후 이용
               #함수는 지역변수가 우선! 그다음이 전역변수다!

def DFS2():
    if cnt==5: #cnt가 지역변수로 없으므로 전역 변수
        print(cnt) #5

def DFS3():
    cnt=3 #DFS3 함수의 지역변수 cnt를 만들었다.
    print(cnt) #3

def DFS4():
    if cnt==5:
        cnt=cnt+1 #'cnt=' 이 있으면 지역변수가 생겼다고 인터프리터가 변역하는데
                  # if cnt=5에서 cnt를 사용했으므로 (UnboundLocalError: local variable 'cnt' referenced before assignment)
        print(cnt)

#해결책

def DFS5():
    global cnt #cnt는 여기서 전역변수라고 알려줌    
    if cnt==5:
        cnt=cnt+1 #기존의 전역변수에 1을 더해 새롭게 전역변수값을 바꾼다고 해석하지
                  # cnt=이걸보고 지역변수 cnt가 생긴다고 생각안하게 된다.
        print(cnt)
        
        
if __name__ =="__main__":
    cnt=5 #전역변수 cnt 생성과 5 할당 
    DFS1()
    DFS2()
    DFS3()
    DFS4()
    DFS5()
    print(cnt)

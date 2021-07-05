#잠깐지식(전역변수와 지역변수)-리스트

def DFS1():
    a[0]=7 #새 리스트를 생성한다는 것이 아니라 a의 0번인덱스의 값을 변경한다는 것
           #따라서 지역이 아닌 전역리스트로 그냥 인식하는것
    print(a)

def DFS2():
    a=[7, 8] #이렇게 선언시에만 지역리스트가 선언됨
    print(a)

def DFS3():
    a=a+[4] #'a='여기서 지역 리스트를 선언한다는 의미인데 등호뒤의
            #지역 리스트a가 선언되지 않은 상태
            #UnboundLocalError: local variable 'a' referenced before assignment

#해결책

def DFS4():
    global a #전역 리스트를 쓰겠다는 의미
    a = a+[4] #여기서는 지역 리스트가 선언안됨. 전역리스트에 더해준다는 의미
    print(a) #[1,2,3,4]
    
if __name__=="__main__":
    a=[1, 2, 3]
    DFS1()
    DFS2()
    DFS3()
    print(a)

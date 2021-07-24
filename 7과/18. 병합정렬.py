#18. 병합정렬, 합병정렬, merge sort
#시간복잡도 O(n logn)
#Divide and conquer 분할과 정복
#후위순회방식-왼쪽자식 호출, 오른쪽자식 호출, 본연의 일 순으로 수행

#D는 2갈래로 뻗는 작업 수행 후에 2개 작업이 끝나고 올라오면 본연의 일을 하는데
#나눠진 두 부분을 합쳐준다.

def Dsort(lt, rt):
    if lt<rt:
        mid=(lt+rt)//2
        Dsort(lt, mid) #두갈래로 뻗어준다. 왼쪽 자식
        Dsort(mid+1, rt) #오른쪽 자식

        #본연의 일
        p1=lt
        p2=mid+1
        tmp=[]
        
        while p1<=mid and p2<=rt:
            if arr[p1]<arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid: #p1이 남은 경우
            tmp=tmp+arr[p1:mid+1] #리스트 합치기
        if p2<=rt:
            tmp=tmp+arr[p2:rt+1]

        for i in range(len(tmp)):
            arr[lt+i]=tmp[i]



if __name__=="__main__":
    arr=[23, 11, 45, 36, 15, 67, 33, 21]
    print("BEFORE SORT : ", end='')
    print(arr)
    Dsort(0, 7) #0번인덱스부터 7번인덱스까지 자료를 정렬해라
    print()
    print("AFTER SORT : ", end='')
    print(arr)

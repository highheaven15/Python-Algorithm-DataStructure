#19. 퀵 정렬, quick sort
#시간복잡도 O(n logn)
#Divide and conquer 분할과 정복
#전위순회방식-본연의 일(분할), 왼쪽자식 호출, 오른쪽자식 호출 순으로 수행


def Qsort(lt, rt):
    if lt<rt:
        #본연의 일
        pos=lt
        pivot=arr[rt] #영역의 가장 오른쪽 것
        for i in range(lt, rt):
            if arr[i]<=pivot:
                arr[i], arr[pos]=arr[pos], arr[i]
                pos+=1
        arr[rt], arr[pos]=arr[pos], arr[rt]
        #파티션 작업 끝
        Qsort(lt, pos-1) #왼쪽 자식 호출
        Qsort(pos+1, rt) #오른쪽 자식 호출

if __name__=="__main__":
    arr=[45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("BEFORE SORT : ", end='')
    print(arr)
    Qsort(0, 9) #0번인덱스부터 9번인덱스까지 자료를 정렬해라
    print()
    print("AFTER SORT : ", end='')
    print(arr)

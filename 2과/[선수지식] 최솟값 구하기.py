#[선수지식] 최솟값 구하기

#1
arr=[5, 3, 7, 9, 2, 5, 2, 6]

arrMin=float('inf') #파이썬에서 가장 큰 값으로 초기화, 무한대값대입

for i in range(len(arr)):
    if arr[i] < arrMin: #등호 같은 경우는 최솟값의 순서가 중요한지에 따라..
        arrMin = arr[i]

print(arrMin)

#2
arr=[5, 3, 7, 9, 2, 5, 2, 6]

arrMin=arr[0]

for i in range(1, len(arr):
    if arr[i] < arrMin:
        arrMin = arr[i]

print(arrMin)               

#3
arr=[5, 3, 7, 9, 2, 5, 2, 6]

arrMin=arr[0]

for x in arr:
    if x <arrMin: 
        arrMin = x

print(arrMin)

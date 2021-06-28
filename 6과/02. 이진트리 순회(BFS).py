#02. 이진트리 순회(BFS)
import sys
sys.stdin = open("input.txt", "rt")

#대부분의 DFS는 전위순회, 병합정렬은 후위순회, 중위순회는 잘 안쓰인다

def DFS(v):
    if v>7:
        return
    else:
        #전위순회
        print(v, end=" ") #출력=함수 본연의 일
        DFS(v*2) #왼쪽 노드 호출
        DFS(v*2+1) #오른쪽 노드 호출
        

if __name__=="__main__":
    DFS(1)


''' 중위순회
        print(v, end=" ") #출력=함수 본연의 일
        DFS(v*2) #왼쪽 노드 호출
        DFS(v*2+1) #오른쪽 노드 호출
'''
''' 후위순회
        print(v, end=" ") #출력=함수 본연의 일
        DFS(v*2) #왼쪽 노드 호출
        DFS(v*2+1) #오른쪽 노드 호출
'''

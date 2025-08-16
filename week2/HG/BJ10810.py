# 공넣기
#시간복잡도 : O(M * N)

N,M = map(int,input().split())
arr = [0] * N #반복문 밖에서 생성

for i in range(1,M+1):
    i,j,k = map(int,input().split())
    for r in range(i, j+1):
        arr[r-1] = k #배열 인덱스는 0부터시작

print(*arr,end=" ")
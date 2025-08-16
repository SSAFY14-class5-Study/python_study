# 공바꾸기

N,M = map(int,input().split())
#바구니안에는 N번 번호가 적힌 공 1개 있음
#빈 배열에 각 번호가 적힌 공을 넣기
arr = []
for r in range(1, N+1):
    arr.append(r)


for c in range(1,M+1): #공 교환 횟수는 M
    i,j = map(int,input().split())
    arr[i-1],arr[j-1] = arr[j-1],arr[i-1] #배열인덱스는 0부터시작인데, 바구니번호는 1부터시작. 
# 해당 바구니 번호 접근하려면 -1 해야함.
print(*arr,end=" ")
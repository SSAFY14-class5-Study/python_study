# 바구니 뒤집기

N, M = map(int, input().split())
arr = []
# 바구니에 번호 달기
for i in range(1, N + 1):  # 1번째 바구니에 1번 번호 적힘
    arr.append(i)


for i in range(1, M + 1):  # 순서바꾸는 횟수 M
    i, j = map(int, input().split())
    arr[i - 1 : j] = arr[i - 1 : j][::-1]  # 할당. 값 바꿔치기
    # 슬라이싱 주의. 바구니는 1부터, 인덱스는 i부터

print(*arr)

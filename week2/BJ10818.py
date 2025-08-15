# 최소,최대
# 시간 복잡도 : O(N)

N = int(input())
num = list(map(int, input().split()))

min_v = num[0]
max_v = num[0]  # 0번 인덱스가 최소,최대값이라고 가정(초기화)

for i in range(1, N):  # num[0]은 이미 초기화에 사용
    if num[i] < min_v:
        min_v = num[i]

    if num[i] > max_v:
        max_v = num[i]

print(min_v, max_v)

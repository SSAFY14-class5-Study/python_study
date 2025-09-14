# 수열

# N은 온도를 측정한 전체 날짜 수
# K는 합을 구하기 위한 연속적인 날짜의 수

# import sys

# N, K = map(int, sys.stdin.readline().split())    # N: 2이상 100,000
# # K: 1과 N(100,000) 사이의 정수


# # 측정한 온도 리스트
# temp = list(map(int, sys.stdin.readline().split()))

# mx_temp = 0     # 최댓값 비교

# for start in range(0, N-K+1):   # start 지점을 그냥 잡고
#     sum_temp = 0

#     for i in range(start, start + K):   # 거기서 K개씩 더함
#         sum_temp += temp[i]

#     # 최댓값 찾기
#     if mx_temp < sum_temp: 
#         mx_temp = sum_temp

# print(mx_temp)


import sys

N, K = map(int, sys.stdin.readline().split())    # N: 2이상 100,000
# K: 1과 N(100,000) 사이의 정수


# 측정한 온도 리스트
temp = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * N

prefix_sum[0] = temp[0]

for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + temp[i]

mx_temp = -float('inf')

if prefix_sum[K-1] > mx_temp:
    mx_temp = prefix_sum[K-1]

for i in range(K, N):
    curr_sum = prefix_sum[i] - prefix_sum[i-K]
    if curr_sum > mx_temp:
        mx_temp = curr_sum


print(mx_temp)
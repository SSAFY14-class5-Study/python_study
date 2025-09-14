# 백준 2491. 수열

N = int(input())    # 수열의 길이
arr = list(map(int, input().split()))

temp_in = 1         # 증가하는 경우의 임시 결과
temp_de = 1         # 감소하는 경우의 임시 결과
in_length = 1       # 증가하는 경우의 결과
de_length = 1       # 감소하는 경우의 결과

for i in range(N-1):
    # 증가하는 경우
    if arr[i] <= arr[i+1]:
        temp_in += 1
    elif arr[i] > arr[i+1]:
        in_length = max(in_length, temp_in)
        temp_in = 1

for i in range(N-1):
    # 감소하는 경우
    if arr[i] >= arr[i+1]:
        temp_de += 1
    elif arr[i] < arr[i+1]:
        de_length = max(de_length, temp_de)
        temp_de = 1
    
in_length = max(in_length, temp_in)
de_length = max(de_length, temp_de)
max_length = max(in_length, de_length)

print(max_length)
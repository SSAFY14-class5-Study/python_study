N = int(input())
num_lst = list(map(int, input().split()))

b_cnt = 1   # 증가 수열 길이
c_cnt = 1   # 감소 수열 길이
mx_cnt = 1  # 최대 길이

for i in range(N-1):
    # 커지는 수열
    if num_lst[i+1] >= num_lst[i]:
        b_cnt += 1
    else:
        b_cnt = 1

    # 작아지는 수열
    if num_lst[i+1] <= num_lst[i]:
        c_cnt += 1
    else:
        c_cnt = 1

    mx_cnt = max(mx_cnt, b_cnt, c_cnt)

print(mx_cnt)

# 팰린드롬인지 확인하기 (회문)
N = list(input())

if N == N[::-1]:
    print(1)
else:
    print(0)
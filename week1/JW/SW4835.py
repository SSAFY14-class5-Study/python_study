# [파이썬 S/W 문제해결 기본] 1일차 - 구간합

T = int(input())

for _ in range(1, T + 1):
    # N : 정수 개수,  M : 구간의 개수
    N, M = list(map(int, input().split()))
    # 정수 N개를 num_list에 추가
    num_list = list(map(int, input().split()))

    # 가상의 최댓값과 최솟값 설정
    max_value = -9999999
    min_value = 9999999

    # 구간별 합계 구하기
    for i in range(N - M + 1):
        total = sum(num_list[i : i + M])
        # 구간합에 따라 최댓값, 최솟값 변경
        if total > max_value:
            max_value = total
        if total < min_value:
            min_value = total

    print(f"#{_} {max_value - min_value}")

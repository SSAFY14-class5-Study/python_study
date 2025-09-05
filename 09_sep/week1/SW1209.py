# 1209. [S/W 문제해결 기본] 2일차 - Sum

for tc in range(1, 11):   # 테스트케이스는 항상 10개
    _ = int(input())

    arr = []
    for _ in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)

    max_val = 0
    # 1. 가로
    for r in range(100):
        temp_max_val = 0
        for c in range(100):
            temp_max_val += arr[r][c]
        if max_val < temp_max_val:
            max_val = temp_max_val

    # 2. 세로
    for c in range(100):
        temp_max_val = 0
        for r in range(100):
            temp_max_val += arr[r][c]
        if max_val < temp_max_val:
            max_val = temp_max_val

    # 우하향 대각선
    temp_max_val = 0
    for i in range(100):
        temp_max_val += arr[i][i]
    if max_val < temp_max_val:
        max_val = temp_max_val

    # 좌하향 대각선
    temp_max_val = 0
    for i in range(100):
        temp_max_val += arr[i][100-1-i]
    if max_val < temp_max_val:
        max_val = temp_max_val

    print(f'#{tc} {max_val}')

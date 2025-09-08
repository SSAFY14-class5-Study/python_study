# [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

T = int(input())

for tc in range(1, T + 1):
    # 색칠할 빈 리스트 생성
    arr = []
    for _ in range(10):
        arr_column = [0] * 10
        arr.append(arr_column)

    N = int(input())  # 칠할 영역의 개수
    # 색깔 딕셔너리 생성
    color_dict = {"color_1": [], "color_2": []}

    # input값을 좌표와 색상으로 나눠서 입력받음
    for i in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))

        # 색칠하기
        # 빨강:1, 파랑:2, 보라:3(1+2)
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                arr[r][c] += color

    cnt = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:  # 컬러가 3(보라)인 곳의 개수 세기
                cnt += 1

    print(f"#{tc} {cnt}")

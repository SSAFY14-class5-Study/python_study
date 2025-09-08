# 파리퇴치3

T = int(input())

for tc in range(1, T + 1):
    # N: 배열 크기, M: 스프레이 세기
    N, M = map(int, input().split())

    # 파리 개수 input을 받아서 리스트 생성
    fly_arr = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        fly_arr.append(arr)

    # 십자(+) 모양
    # 델타값 설정 : 상 > 우 > 하 > 좌 (시계방향)
    dr_1 = [-1, 0, 1, 0]
    dc_1 = [0, 1, 0, -1]

    # 가상의 결과값을 0으로 설정
    max_value_1 = 0

    for R in range(N):
        for C in range(N):
            # 노즐 중심값을 임시 합계 초기값으로 지정
            total = fly_arr[R][C]

            for d in range(4):  # 4 = 델타 리스트 길이
                for m in range(1, M):
                    # 스프레이 세기를 고려한 새로운 좌표값 설정
                    nr = R + dr_1[d] * m
                    nc = C + dc_1[d] * m

                    if 0 <= nr < N and 0 <= nc < N:
                        total += fly_arr[nr][nc]

            if max_value_1 < total:
                max_value_1 = total

    # 대각선(X) 모양
    # 델타값 설정
    dr_2 = [-1, -1, 1, 1]
    dc_2 = [-1, 1, 1, -1]

    # 가상의 결과값을 0으로 설정
    max_value_2 = 0

    for R in range(N):
        for C in range(N):
            # 노즐 중심값을 임시 합계 초기값으로 지정
            total = fly_arr[R][C]

            for d in range(4):  # 4 = 델타 리스트 길이
                for m in range(1, M):
                    # 스프레이 세기를 고려한 새로운 좌표값 설정
                    nr = R + dr_2[d] * m
                    nc = C + dc_2[d] * m

                    if 0 <= nr < N and 0 <= nc < N:
                        total += fly_arr[nr][nc]

            if max_value_2 < total:
                max_value_2 = total

    if max_value_1 < max_value_2:
        result = max_value_2
    else:
        result = max_value_1

    print(f"#{tc} {result}")

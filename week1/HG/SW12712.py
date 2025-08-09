# 파리퇴치 3

T = int(input())

dr_plus = [-1, 1, 0, 0]  # 좌 우 상 하
dc_plus = [0, 0, -1, 1]

dr_multi = [-1, -1, 1, 1]  # 좌상 좌하 우하 우상
dc_multi = [-1, 1, 1, -1]

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    # 모든 배열을 순회해야함.
    for R in range(N):  #
        for C in range(N):

            # 현재 파리합계
            crr_val = arr[R][C]
            for r in range(4):  # 4방향 순회
                for c in range(1, M):  # 스프레이 분사도 만큼
                    nr = R + dr_plus[r] * c  # r : 방향
                    nc = C + dc_plus[r] * c
                    if (
                        0 <= nr < N and 0 <= nc < N
                    ):  # 범위 안에 있다면, 현재 파리합계에 각 칸의 파리수 더함
                        crr_val += arr[nr][nc]  # 각 칸에 더함
                if crr_val > max_val:
                    max_val = crr_val

                crr_val_2 = arr[R][C]
                for r in range(4):
                    for c in range(1, M):
                        nr = R + dr_multi[r] * c
                        nc = C + dc_multi[r] * c
                        if 0 <= nr < N and 0 <= nc < N:
                            crr_val_2 += arr[nr][nc]
                if crr_val_2 > max_val:
                    max_val = crr_val_2
    print(f"#{tc} {max_val}")

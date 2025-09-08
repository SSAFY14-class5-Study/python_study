# 파리 퇴치 3
T = int(input())

# +
dr_plus = [-1, 1, 0, 0]
dc_plus = [0, 0, -1, 1]

# x
dr_multiple = [-1, 1, -1, 1]
dc_multiple = [-1, 1, 1, -1]

for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for r in range(N):
        for c in range(N):
            sum_fly = arr[r][c]

            for d in range(4):
                for m in range(1, M):
                    nr = r + dr_plus[d] * m 
                    nc = c + dc_plus[d] * m 

                    if 0 <= nr < N and 0 <= nc < N:
                        sum_fly += arr[nr][nc]
                    
            if max_v < sum_fly:
                max_v = sum_fly
                    
            sum_fly = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr_multiple[d] * m 
                    nc = c + dc_multiple[d] * m 

                    if 0 <= nr < N and 0 <= nc < N:
                        sum_fly += arr[nr][nc]
                    
            if max_v < sum_fly:
                max_v = sum_fly

    # 출력
    print(f"#{tc} {max_v}")
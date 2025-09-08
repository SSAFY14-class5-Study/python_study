# 파리 퇴치3
T = int(input())    # 테스트 케이스

# + 델타 (상하좌우)
dr_plus = [-1, 1, 0, 0]
dc_plus = [0, 0, -1, 1]

# * 델타 (대각선)
dr_multi = [-1, -1, 1, 1]
dc_multi = [-1, 1, -1, 1]


for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 배열 생성
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = -float('inf')   # 최대값 비교 변수
    
    for r in range(N):
        for c in range(N):
            sum_fly = arr[r][c]     # 기준점

            # 상하좌우 검사
            for d in range(4):      # 델타 돌면서
                for m in range(1, M):   # 기준점 제외하고 M만큼
                    nr = r + dr_plus[d] * m
                    nc = c + dc_plus[d] * m
            
                    # 범위 체크
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_fly += arr[nr][nc]

            # 최댓값 비교
            if sum_fly > max_v:
                max_v = sum_fly


            sum_fly = arr[r][c]     # 구분 위해 변수 다시 초기화
            # 대각선 검사
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr_multi[d] * m
                    nc = c + dc_multi[d] * m

                    # 범위 체크
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_fly += arr[nr][nc]

            # 최댓값 비교
            if sum_fly > max_v:
                max_v = sum_fly

    # 출력
    print(f"#{tc} {max_v}")
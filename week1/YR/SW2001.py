# 파리 퇴치
T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 2차원 배열 입력 받기
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0   # 최댓값 비교 변수

    # 기준점 (r, c)
    for r in range(N-M+1):
        for c in range(N-M+1):

            sum_fly = 0    # 파리 변수
            for x in range(r, r+M):     # 기준점에서 +M 만큼 돌면서
                for y in range(c, c+M):
                    sum_fly += arr[x][y]    # 파리 더하기

            if sum_fly > max_v:
                max_v = sum_fly

    # 출력
    print(f"#{tc} {max_v}")
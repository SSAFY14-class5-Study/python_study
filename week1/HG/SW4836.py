# 색칠하기

T = int(input())

for tc in range(1, T + 1):
    grid = [[0] * 10 for _ in range(10)]
    N = int(input())
    # n개의 색칠 정보 받기
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for R in range(r1, r2 + 1):  # 빈 격자 모든 칸 순회(R,C)
            for C in range(c1, c2 + 1):
                grid[R][C] += color  # 위에서 1줄로 입력받은 그 색으로 칠함
                # 파랑,빨강 겹치는 칸은 보라 값 3 가짐

    purple_count = 0  # 초기화
    for R in range(10):
        for C in range(10):
            if grid[R][C] == 3:  # 만약 보라색이면
                purple_count += 1

    print(f"#{tc} {purple_count}")

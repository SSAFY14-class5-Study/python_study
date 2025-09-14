# 10580. 전봇대

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 전선의 개수

    wires = []          # 전선 저장할 리스트
    result_cnt = 0      # 교차점 개수

    for _ in range(N):
        start, end = map(int, input().split())

        for prev_start, prev_end in wires:
            # 1. 기존의 시작점보다 높고, 기존의 도착점보다 낮은 경우
            if start > prev_start and end < prev_end:
                result_cnt += 1

            # 2. 기존의 시작점보다 낮고, 기존의 도착점보다 높은 경우
            if start < prev_start and end > prev_end:
                result_cnt += 1

        # 리스트에 저장
        wires.append((start, end))

    print(f'#{tc} {result_cnt}')
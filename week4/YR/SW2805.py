# 농작물 수확하기
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr=[list(map(int, input())) for _ in range(N)]
    earn = 0
    mid = N // 2

    for r in range(N):
        if r <= mid:
            start = mid-r
            end = N - (mid-r)

        else:
            start = r - mid
            end = N - (r-mid)

        for c in range(start, end):
            earn += arr[r][c]

    # 출력
    print(f"#{tc} {earn}")
# 농작물 수확하기
T = int(input())

for tc in range(1, T+1):

    N = int(input())    # 농작물 크기
    farm = [list(map(int, input().strip())) for _ in range(N)]

    mid = N // 2
    
    revenue = 0

    for r in range(N):
        if r <= mid:
            start = mid - r
            end = N - (mid - r)
        else:
            start = r - mid
            end = N - (r - mid)

        for c in range(start, end):
            revenue += farm[r][c]

    # 출력
    print(f"#{tc} {revenue}")
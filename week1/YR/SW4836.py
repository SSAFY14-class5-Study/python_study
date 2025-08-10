T = int(input())  # 테스트 케이스

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]  # 10x10 배열
    purple = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        
        # 범위 설정
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color

    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:  # 빨강(1) + 파랑(2) = 3
                purple += 1     # 보라색 카운트

    # 출력
    print(f"#{tc} {purple}")

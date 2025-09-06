# Magnetic

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for c in range(N):
        seen = False

        for r in range(N):
            magnetic = arr[r][c]
            if magnetic == 1:
                seen = True
            
            elif magnetic == 2:
                if seen:
                    cnt += 1
                    seen = False    # 초기화

    print(f"#{tc} {cnt}")
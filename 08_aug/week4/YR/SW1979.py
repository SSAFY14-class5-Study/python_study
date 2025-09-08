# 어디에 단어가 들어갈 수 있을까
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for r in range(N):
        runword = 0
        for c in range(N):
            if arr[r][c] == 1:
                runword += 1
            else:
                if runword == K:
                    ans += 1
                runword = 0
        if runword == K:
            ans += 1


    for c in range(N):
        runword = 0
        for r in range(N):
            if arr[r][c] == 1:
                runword += 1
            else:
                if runword == K:
                    ans += 1
                runword = 0

        if runword == K:
            ans += 1


    print(f"#{tc} {ans}") 
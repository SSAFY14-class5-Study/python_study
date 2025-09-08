def count_words(puzzle, N, K):
    count = 0

    # horizontal
    for r in range(N):
        run = 0
        for c in range(N):
            if puzzle[r][c] == 1:
                run += 1
            else:
                if run == K:
                    count += 1
                run = 0  
        if run == K:
            count += 1

    # vertical
    for c in range(N):
        run = 0
        for r in range(N):
            if puzzle[r][c] == 1:
                run += 1
            else:
                if run == K:
                    count += 1
                run = 0
        if run == K:
            count += 1                
    return count



T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    ans = count_words(puzzle, N, K)
    print(f'#{tc} {ans}')

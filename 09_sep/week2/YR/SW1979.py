# 어디에 단어가 들어갈 수 있을까
T = int(input())

for tc in range(1, T+1):    # 테스트 케이스

    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0     # 자리 수

    # 가로 검사
    for r in range(N):
        runone = 0      # 자리 판별 (연속된 1의 개수가 k개인지)
        
        for c in range(N):
            if arr[r][c] == 1:
                runone += 1
            else:
                if runone == K:
                    cnt += 1
                runone = 0      # 다시 초기화

        # 끝이라 0을 만나지 않고 조건을 충족한 경우 (for문 실행 뒤 1번 실행됨)      
        if runone == K:
            cnt += 1
            runone = 0


    # 세로 검사
    for c in range(N):
        runone = 0      # 자리 판별
        
        for r in range(N):
            if arr[r][c] == 1:
                runone += 1
            else:
                if runone == K:
                    cnt += 1
                runone = 0

        # 끝이라 0을 만나지 않고 조건을 충족한 경우 (for문 실행 뒤 1번 실행됨)      
        if runone == K:
            cnt += 1
            runone = 0

    # 출력
    print(f"#{tc} {cnt}")
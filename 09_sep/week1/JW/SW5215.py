# 5215. 햄버거 다이어트

T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    # N : 재료의 수
    # L : 제한 칼로리

    # 리스트에 재료 정보 입력
    arr = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)

    max_kcal = -1

    # dfs 함수 정의
    def dfs(i, score, kcal):
        global max_kcal

        # 중단 조건 - 1. 제한 칼로리를 초과한 경우
        if kcal > L:
            return
        # 중단 조건 - 2. 탐색을 모두 완료한 이후
        if i == N:
            if max_kcal < score:
                max_kcal = score
            return
        
        # 재귀 호출
        # 1. 현재(i) 재료 선택 : score, kcal에 i번째 항목 더하기
        dfs(i+1, score + arr[i][0], kcal + arr[i][1])
        # 2. 현재(i) 재료 선택 X
        dfs(i+1, score, kcal)
    
    dfs(0, 0, 0)
    
    print(f'#{tc} {max_kcal}')
    
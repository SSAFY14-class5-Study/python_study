# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
        
def recur(row, result):
    global min_cost

    # 가지치기
    if result >= min_cost:
        return

    # 재귀함수 기저조건
    if row == N:    # N개의 제품을 모두 고려한 경우 종료
        min_cost = min(min_cost, result)    # 최소값 업데이트
        return

    # 공장 선택하기
    for col in range(N):    # row: 제품  # col: 공장
        if visited[row][col] == 0:  # 아직 방문하지 않았다면(0)
            for r in range(N):      # 그 다음 열(r)부터는 선택되지 않도록 1로 변경
                visited[r][col] = 1

            visited[row][col] = 1   # 현위치를 방문처리(1)
            recur(row + 1, result + cost_arr[row][col])

            # 백트래킹 (원상복구)
            for r in range(N):
                visited[r][col] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # N : 제품 수
    cost_arr = [list(map(int, input().split())) for _ in range(N)]  # 공장별 생산비용
    visited = [[0] * N for _ in range(N)]   # 공장 선택 여부 확인할 배열 생성
    
    min_cost = 9999999
    recur(0, 0)
    print(f'#{tc} {min_cost}')
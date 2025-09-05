# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 미로 배열 크기

    maze = []
    for _ in range(N):
        temp = list(map(int, input()))
        maze.append(temp)
        
    # 방문처리 배열
    visited = [[False]*N for _ in range(N)]

    # 시작점과 도착점 좌표
    start_r, start_c, end_r, end_c = -1, -1, -1, -1
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r = r
                start_c = c
            elif maze[r][c] == 3:
                end_r = r
                end_c = c

    # 델타(상하좌우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # BFS
    q = deque()

    visited[start_r][start_c] = True    # 시작점 방문 저리
    q.append((start_r, start_c))     # 노드(튜플) : (r, c)

    can_reach = False   # 목적지(3) 도달 여부
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 경계조건 내부인가
            if 0 <= nr < N and 0 <= nc < N:
                # 통로(0)면서 방문하지 않은 경우
                if maze[nr][nc] == 0 and visited[nr][nc] == False:
                    visited[nr][nc] = True
                    q.append((nr, nc))

                # 도착지점(3)에 도착한 경우
                if maze[nr][nc] == 3:
                    can_reach = True

    if can_reach == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

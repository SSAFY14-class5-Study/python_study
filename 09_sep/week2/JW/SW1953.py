# 1953. [모의 SW 역량테스트] 탈주범 검거

from collections import deque

# 델타배열 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 터널별 델타 적용
types = {
    1 : [1, 1, 1, 1],   # 상하좌우
    2 : [1, 1, 0, 0],   # 상하
    3 : [0, 0, 1, 1],   # 좌우
    4 : [1, 0, 0, 1],   # 상우
    5 : [0, 1, 0, 1],   # 하우
    6 : [0, 1, 1, 0],   # 하좌
    7 : [1, 0, 1, 0]    # 상좌
}

def bfs(R, C):
    q = deque([(R, C)])     # 후보군
    visited[R][C] = 1       # 출발점 초기화

    while q:  # 후보군이 없을 때까지 반복
        now_r, now_c = q.popleft()
        dirs = types[arr[now_r][now_c]]

        for d in range(4):
            # 출구가 없는 경우 pass
            if dirs[d] == 0:
                continue

            # 다음 좌표
            new_r = now_r + dr[d]
            new_c = now_c + dc[d]

            # 범위 밖이면 pass
            if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
                continue

            # 못 가는 곳이면 pass
            if arr[new_r][new_c] == 0:
                continue

            # 이미 방문한 경우 pass
            if visited[new_r][new_c]:
                continue

            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[arr[new_r][new_c]]

            # 현재 위치와 이동할 위치가 뚫려있는지 확인
            # - 상->하  좌->우
            if d % 2 == 0 and next_dirs[d+1] == 0:
                continue
            # - 하->상  우->좌
            if d % 2 == 1 and next_dirs[d-1] == 0:
                continue

            # L 시간 이후의 좌표는 pass
            if visited[now_r][now_c] + 1 > L:
                continue

            # 시간을 +1 하며 기록
            visited[new_r][new_c] = visited[now_r][now_c] + 1
            q.append((new_r, new_c))


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    bfs(R, C)
    cnt = 0

    # L 시간 이하로 방문한 모든 곳을 count
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1
    
    print(f'#{tc} {cnt}')
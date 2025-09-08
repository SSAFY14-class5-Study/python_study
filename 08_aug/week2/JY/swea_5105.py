from collections import deque

def find_distance(maze,N):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    start_r, start_c, end_r, end_c = -1, -1, -1, -1
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r, start_c = r, c
            elif maze[r][c] == 3:
                end_r, end_c = r, c

    visited = [[False]*N for _ in range(N)]
    queue = deque()
    visited[start_r][start_c] = True
    queue.append((start_r, start_c, 0))

    can_go = False
    final_distance = 0

    while queue:
        r,c, distance = queue.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr,nc, distance + 1))
                if maze[nr][nc] == 3:
                    can_go = True
                    final_distance = distance
    return final_distance
                    
    

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # [int(n) for n in "13101"]
    # [1, 3, 1, 0, 1]
    maze = [[int(n)for n in input()] for _ in range(N)]
    ans = find_distance(maze,N)
    print(f'#{tc} {ans}')
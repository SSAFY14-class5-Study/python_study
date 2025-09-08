# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # V = 노드의 개수
    # E = 간선의 개수

    # 인접 리스트 생성 및 input값 입력 받기
    adj = [0]
    for _ in range(V):
        adj.append([])

    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    S, G = map(int, input().split())
    # S = 출발 지점
    # G = 도착 지점

    # 방문처리 배열과 큐 생성
    visited = [0] * (V + 1)     # 방문처리 배열(거리 계산)
    queue = deque()             # 인접 노드를 저장할 큐

    # 1. 시작점 S를 큐에 삽입
    visited[S] = 0      # 시작 정점의 거리 = 0
    queue.append(S)

    # 2. 큐에 아무것도 남아있지 않을 때까지 while문 반복
    while queue:
        v = queue.popleft()

        if v == G:  # 도착 지점에 이르면
            break   # 종료

        # 인접 노드(w) 탐색
        for w in adj[v]:
            if visited[w] == 0:             # 방문하지 않았다면
                visited[w] = visited[v] + 1 # 거리 갱신
                queue.append(w)             # 큐에 추가한 뒤 다음 탐색으로 넘어감

    if visited[G] == 0:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} {visited[G]}")

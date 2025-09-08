# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접노드 리스트 생성
    adj = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = list(map(int, input().split()))
        adj[start].append(end)

    S, G = map(int, input().split())

    stack = []
    connected = False       # 우선 연결되지 않았다고 가정

    # 방문처리 배열
    visited = [0] * (V+1)   # 방문한 뒤에 1로 변경

    # 시작점(S) 방문
    visited[S] = 1
    stack.append(S)

    while stack:
        v = stack.pop()

        if v == G:              # 도착지점에 도착 후
            connected = True    # 연결되었다(True)고 변경 후 중단(break)
            break
        
        for n in adj[v]:            # v의 인접노드(n)에 아직 방문하지 않은 경우
            if visited[n] == 0:
                visited[n] = 1      # 방문 처리
                stack.append(n)

    if connected:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
        
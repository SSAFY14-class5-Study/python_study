# 알고리즘 수업 - 너비 우선 탐색
from collections import deque

def bfs(start_node): #너비 우선탐색 + 각 노드의 방문 순서 기록하는 함수
    count = 1 #초기화 1번째 방문부터 시작

    my_q = deque([start_node])
    visited[start_node] = count

    while my_q:
        u = my_q.popleft() 
        #현재노드 u 에 인접한 모든 노드 v를 확인
        for v in graph[u]:
            if visited[v] == 0: #미방문노드이면
                count += 1
                visited[v] = count #v의 방문순서 저장
                my_q.append(v)

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1) # 방문순서를 기록하며, 0이 아니면 방문한거임

#그래프 생성
for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

bfs(R)

for i in range(1,N+1):
    print(visited[i])







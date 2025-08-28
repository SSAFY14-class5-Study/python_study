T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    
    # 그래프를 어떻게 저장할 것인가?
    # 인접행렬 또는 인접리스트로 저장

    # 인접리스트인 경우
    # 노드 번호가 1번부터 ~ V번까지
    # 각 노드에 연결되어 있는 노드의 번호를 리스트에 저장
    # => 2차원 리스트

    adj = [[] for _ in range(V+1)]
    # adj[1] : 1번과 연결되어 있는 노드 번호들
    # adj[V] : V번 노드와 연결되어 있는 노드 번호들

    for _ in range(E): # E개의 간선 정보를 입력받는다. 
        start, end = list(map(int,input().split()))
        adj[start].append(end) # start -> end 간선을 인접리스트로 

    S, G = list(map(int,input().split()))
    # S : 출발점
    # G : 도착점

    # S와 G가 서로 연결되었는지?
    # S를 출발점으로해서 그래프 탐색
    # 그래프 탐색: 그래프의 모든 노드를 한 번씩 방문
    # 그래프 탐색을 하는 도중에 G가 발견이 됨: S, G는 연결됨
    # 그래프 탐색이 끝났음에도 G가 발견안됨 : S에서 출발해서 G로 

    stack =[] # DFS 탐색을 위해, 인접 노드를 저장할스택
    connected = False  # 연결 안됨으로 가정
    # 중간에 G가 나오면 True로 바꿔주기

    visited=[0] * (V+1)
    
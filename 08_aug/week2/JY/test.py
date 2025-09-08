# 1. 정확한 반복 횟수가 안 나와 있고, 반복의 조건만 나와있다면 => while
# 2. 방문처리(visited)
# N = 5 방의 개수 5개, 1번 ~ 5번 방까지
# p = [0] + [0, 1, 1, 2, 0] N-1 크기의 배열을 만들고 가장 첫번째는 쓰지 않는다.
# visited = [False] * (N+1)

def count_portal(N,P):
    visited = [False] * (N+1)
    idx = 1
    visited[idx] = True # 1번은 이미 방문한 상태로 시작, 2~N번 방은 아직 방문하지 않은 상태

    # 목표 : idx => N까지 가길 바람(종료조건)
    # <=> 반대되는 상황: idx가 아직 N이 아닌 상황(반복해야 하는 조건)

    while idx < N:
        idx += 1
        cnt += 1

        if not visited[idx]:
            visited[idx] = True
            idx = P[idx]
            cnt += 1
        
        if idx == N:
            break

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    P = [0] + list(map(int,input().split()))

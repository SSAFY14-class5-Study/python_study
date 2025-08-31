# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree

T = int(input())

# 노드 탐색 함수 정의
def f(root):
    global node_cnt

    node_cnt += 1
    if left_c[root] != 0:   # 왼쪽에 자식이 있다면 왼쪽 자식 노드 탐색
        f(left_c[root])
    if right_c[root] != 0:  # 오른쪽에 자식이 있다면 오른쪽 자식 노드 탐색
        f(right_c[root])


for tc in range(1, T+1):
    E, N = map(int, input().split())
    # E : 간선의 개수
    # N : 시작 노드

    left_c  = [0] * (E + 2)
    right_c = [0] * (E + 2)

    arr = list(map(int, input().split()))

    for i in range(E):
        parent = arr[i*2]
        child = arr[i*2 + 1]

        if left_c[parent] == 0:         # 자식이 없는 경우
            left_c[parent] = child      # 왼쪽에 입력
        else:                           # 왼쪽에 이미 자식이 있는 경우
            right_c[parent] = child     # 오른쪽에 입력

    # 노드 개수를 저장할 cnt
    node_cnt = 0

    # 노드 탐색
    f(N)

    print(f'#{tc} {node_cnt}')
    
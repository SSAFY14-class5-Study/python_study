def preorder(v, left_child, right_child):
    # v : 현재 방문할 노드 번호 (예: 1 → 루트, 6 → 1의 왼쪽 자식)
    # left_child : 모든 노드의 "왼쪽 자식 번호"를 저장한 배열
    # right_child : 모든 노드의 "오른쪽 자식 번호"를 저장한 배열

    if v == 0:       # v == 0이면 '자식 없음'을 의미하므로 탐색 종료
        return 0

    count = 1        # 자기 자신 노드 1개 카운트
    # 왼쪽 자식 서브트리의 크기 구하기
    count += preorder(left_child[v], left_child, right_child)
    # 오른쪽 자식 서브트리의 크기 구하기
    count += preorder(right_child[v], left_child, right_child)

    return count     # (자기 자신 + 왼쪽 서브트리 + 오른쪽 서브트리) 합 리턴


def count_subtree_nodes(E, N, data):
    # E : 간선 개수
    # N : 서브트리의 루트가 되는 노드 번호 = 탐색 시작 노드
    # data : [부모1, 자식1, 부모2, 자식2, ...] 형태로 주어진 간선 정보

    # 노드 번호는 1 ~ E+1까지 존재 → 배열 크기는 (E+2)
    left_child = [0] * (E+2)   # left_child[i] = i번 노드의 왼쪽 자식 번호
    right_child = [0] * (E+2)  # right_child[i] = i번 노드의 오른쪽 자식 번호

    # 간선 정보를 배열에 저장
    for i in range(E):
        parent, child = data[2*i], data[2*i+1]
        if left_child[parent] == 0:   # 왼쪽 자식 비어있으면 왼쪽에 저장
            left_child[parent] = child
        else:                         # 이미 있으면 오른쪽 자식에 저장
            right_child[parent] = child

    # N번 노드를 루트로 하는 서브트리 크기 리턴
    return preorder(N, left_child, right_child)


# 메인 실행부
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())       # 간선 개수, 루트 노드 번호
    data = list(map(int, input().split())) # 간선 정보 입력
    ans = count_subtree_nodes(E, N, data)
    print(f'#{tc} {ans}')

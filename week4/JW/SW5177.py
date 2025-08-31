# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 완전 이진 트리
    heap = [0] * (N+1)  # 힙 생성

    nums = list(map(int, input().split()))

    for i, num in enumerate(nums, start=1):
        heap[i] = num

        child_idx = i
        parent_idx = i // 2

        # 부모>자식인 경우 그 두 숫자를 바꾸기
        while parent_idx >= 1 and heap[parent_idx] > heap[child_idx]:
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]

            # 자식 인덱스를 부모 인덱스로 바꿔 조상 탐색
            child_idx = parent_idx
            parent_idx = parent_idx // 2

    # N의 조상 노드 갯수 세기
    sum = 0
    child_idx = N
    parent_idx = child_idx // 2
    while parent_idx >= 1:
        sum += heap[parent_idx]
        parent_idx //= 2

    print(f'#{tc} {sum}')
    
# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색

T = int(input())

# 중위순회(LVR) 함수 정의
def inorder(i):
    global tree, cnt

    left_child = i*2
    right_child = i*2 + 1

    # L : 왼쪽 탐색
    if left_child <= N:
        inorder(left_child)
    
    # V : 현재 노드 방문
    tree[i] = cnt
    cnt += 1

    # R : 오른쪽 탐색
    if right_child <= N:
        inorder(right_child)


for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    cnt = 1

    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')

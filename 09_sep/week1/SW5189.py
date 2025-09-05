# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

# 순열 함수
def f(idx, temp_sum, prev_num):
    # idx: N-1개의 숫자를 뽑는 순서, 0~ N-2번까지 뽑고 N-1이되면 기저조건
    # temp_sum : 앞 재귀함수까지의 합
    # prev_num : 앞의 구역번호
    global result

    # 1. 기저조건
    if idx == N-1:
        temp_sum += arr[prev_num][1]
        if temp_sum < result:
            result = temp_sum
        return

    # 1.2. 가지치기
    if temp_sum >= result:
        return

    # 2. 유도조건
    for num in range(2, N+1):
        if not visited[num]:
            visited[num]= True
            f(idx+1, temp_sum + arr[prev_num][num], num)
            visited[num] = False ###!!!!!


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    arr.append([0]*(N+1))
    visited = [False] * (N+1)   # 방문 여부 확인

    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)

    for r in range(1, N+1):
        arr[r].insert(0, 0)

    result = 9999999
    f(0, 0, 1)

    print(f'#{tc} {result}')
    
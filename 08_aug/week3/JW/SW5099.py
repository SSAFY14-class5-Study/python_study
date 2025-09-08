# [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 치즈 input값을 받아서 튜플로 변형 후 pizzas 리스트에 삽입
    nums = list(range(1, M+1))                  # 피자 인덱스값
    cheeses = list(map(int, input().split()))   # 치즈 양
    pizzas = list(zip(nums, cheeses))

    # 화덕
    q = deque()

    for _ in range(N):
        # 화덕 칸 개수(N) 만큼 피자 집어넣기 
        q.append(pizzas.pop(0))

    # 화덕 내 피자 개수 > 1 인 경우 while문 반복
    while len(q) > 1:
        # 가장 앞에 있는 피자를 꺼내서 치즈 양을 절반으로 줄이기
        num, cheese = q.popleft()
        cheese //= 2

        # 치즈가 다 녹았고(0), 화덕에 넣지 않은 피자가 남아있는 경우
        if cheese == 0 and pizzas:
            q.append(pizzas.pop(0))     # 남아있는 것 중 첫 번째 피자 집어넣기
        # 치즈가 덜 녹았다면 => 다시 화덕에 넣기
        elif cheese > 0:
            q.append((num, cheese))     # 피자 넘버는 그대로, 치즈 양은 절반 줄어든 상태

    # 화덕(q)에서 마지막 피자를 꺼낸다.
    num, cheese = q.popleft()

    print(f"#{tc} {num}")
    
# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N: 컨테이너 수
    # M: 트럭 수

    weight = sorted(list(map(int, input().split())), reverse=True)    # 화물의 무게
    capacity = sorted(list(map(int, input().split())), reverse=True)  # 트럭의 적재용량

    result = 0  # 적재 화물 무게
    
    while len(weight) > 0 and len(capacity) > 0:
        if capacity[0] >= weight[0]:    # 화물 무게보다 적재 용량이 더 크다면
            result += weight[0]         # 트럭에 화물을 넣기
            weight.pop(0)               # 화물 리스트에서 해당 화물 삭제
            capacity.pop(0)             # 트럭 리스트에서 해당 트럭 삭제
        else:                           # 화물 무게가 적재 용량보다 크다면
            weight.pop(0)               # 싣을 수 없으므로 화물 리스트에서 해당 화물 삭제

    print(f'#{tc} {result}')
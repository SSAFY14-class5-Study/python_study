# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

# 충전 횟수 구하는 함수 정의
def cnt_charing(K, N, charging_station):
    cnt = 0
    idx = 0

    while idx < N:
        candidates = []
        for c in charging_station:
            if idx < c <= idx + K:
                candidates.append(c)
        
        # case 1. 현 위치에서 K만큼 이동했을 때 종점에 도착했거나 넘어서는 경우
        if idx + K >= N:
            return cnt
        
        # case 2. 현 위치에서 K만큼 이동했을 때 갈 수 있는 충전기가 없는 경우
        if len(candidates) == 0:
            return 0

        # case 3. 갈 수 있는 충전소가 있다면
        else:
            idx = max(candidates)
            cnt += 1

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K:정류장 수   N:종점   M:충전기 개수

    charging_station = list(map(int, input().split()))  # 충전기 위치

    cnt = cnt_charing(K, N, charging_station)

    print(f'#{tc} {cnt}')
    
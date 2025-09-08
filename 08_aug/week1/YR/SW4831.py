# 전기버스

# 함수
def countCharge(K, N, M, chargers):
    idx = 0     # 버스 0번 정류장에서 출발
    cnt = 0     # 충전횟수
    
    
    while idx < N:
        
        if idx + K >= N:    # 바로 갈 수 있으면 반환
            return cnt

        candidates = [] # 갈 수 있는 충전소 담을 리스트
        for i in chargers:
            if idx < i and i <= idx+K:
                candidates.append(i)
        
        if len(candidates) == 0:    # 충전소 없으면 0
            return 0

        else:
            idx = max(candidates)   # 갈 수 있는 가장 먼 충전소
            cnt += 1        # 충전 카운트 늘리기


T = int(input())    # 노선 수

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))   # N은 정류장, K는 최대 이동 정류장, M은 충전기 정류장 
    chargers = list(map(int, input().split()))  # 충전기 위치

    # 충전횟수
    result = countCharge(K, N, M, chargers)

    # 출력
    print(f"#{tc} {result}")
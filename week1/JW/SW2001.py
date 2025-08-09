# 파리 퇴치

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 파리 개수 input을 받아서 리스트 생성
    fly_arr = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        fly_arr.append(arr)

    # 기초 max값 설정
    max_val = 0
    # 파리채 기본 좌표 설정
    for R in range(N - M + 1):  # 리스트 길이에서 파리채 크기만큼 빼고 +1(range니까!)
        for C in range(N - M + 1):
            # 파리채 한 번 휘둘렀을 때 잡은 파리 개수(fly_total)
            fly_total = 0
            # 파리채 영역 설정
            for r in range(M):
                for c in range(M):
                    fly_total += fly_arr[R + r][C + c]

            # fly_total에서 최대값 찾기
            if max_val < fly_total:
                max_val = fly_total

    print(f"#{tc} {max_val}")

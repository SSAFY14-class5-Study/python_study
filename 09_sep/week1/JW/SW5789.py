# 5789. 현주의 상자 바꾸기

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # N = 상자의 개수
    # Q = 숫자 변경 횟수

    # 초기 상자 리스트 생성
    box = [0] * N

    for i in range(Q):
        L, R = map(int, input().split())
        for k in range(L-1, R):
            box[k] = i+1

    print(f'#{tc}', " ".join(map(str, box)))
    
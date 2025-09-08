# 현주의 상자 바꾸기
T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * (N + 1) 

    for i in range(1, Q + 1):
        L, R = map(int, input().split())

        for k in range(L, R + 1):
            box[k] = i

    print(f"#{tc}", *box[1:])

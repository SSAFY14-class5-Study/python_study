# 증가하는 사탕 수열

T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    candy = 0

    if A > B > C:
        print(f"#{tc} -1")
        continue

    while not (A < B < C):
        if B >= C:
            B -= 1
            candy += 1

        elif A >= B:
            A -= 1
            candy += 1  

    print(f"#{tc} {candy}")
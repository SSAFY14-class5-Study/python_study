# 증가하는 사탕 수열
T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    candy = 0

    while not (A < B < C):
        if C <= 1:
            candy = -1
            break

        if B >= C:
            eat = B - (C - 1) 
            B -= eat
            candy += eat

        elif A >= B:
            if B <= 1:
                candy = -1
                break
            eat = A - (B - 1)  
            A -= eat
            candy += eat

        if A <= 0 or B <= 0:
            candy = -1
            break

    print(f"#{tc} {candy}")


def min_candies_to_eat(A, B, C):
    count = 0

    while not(A < B < C):
        if C <= 1:
            return -1
        
        if B >= C:
            eat = B - (C - 1)
            B -= eat
            count += eat

        elif A >= B:
            if B <= 1:
                return-1
            eat = A - (B - 1)
            A -= eat
            count += eat
        if A <= 0 or B <= 0:
            return -1
    return count

T = int(input())
for tc in range(1,T+1):
    A, B, C = map(int,input().split())
    ans = min_candies_to_eat(A, B, C)
    print(f'#{tc} {ans}')

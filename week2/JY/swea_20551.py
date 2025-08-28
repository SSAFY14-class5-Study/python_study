def count_candy(A,B,C):
    count = 0
    while A and B and C > 0:
        if A < B and B < C:
            return 0
        if A > B:
            if B < C:
                count += A - B -1
            elif C < B:
                count += (B - C - 1) + (A - B - 1)
            

T = int(input())
for tc in range(1,T+1):
    A,B,C = map(int,input().split())
    ans = count_candy(A,B,C)
    print(f'#{tc} {ans}')
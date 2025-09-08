def rotate(numbers,N,M):
    ans = numbers[M%N]
    return ans

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    numbers = list(map(int,input().split()))

    ans = rotate(numbers,N,M)
    print(f'#{tc} {ans}')
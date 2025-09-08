def order_escape(N,K,position):
    rooms = [0] * (N+1)
    for people in position:
        rooms[people] += 1
    
    while sum(rooms) > 0:
        count = 0

        for i in range(1,N+1):
            if rooms[i] > 0:
                d = min(abs(i - 0), abs(i - (N+1)))
                count += d
                rooms[i] = 0

        if sum(rooms) == 0:
            break
    return count

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    position = list(map(int,input().split()))
    ans = order_escape(N,K,position)
    print(f'#{tc} {ans}')


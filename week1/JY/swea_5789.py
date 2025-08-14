
T = int(input())
for tc in range(1,T+1):
    N,Q = map(int, input().split())
    boxes = [0] * N
    for work in range(1,Q+1):
        L,R = map(int,input().split())
        for num in range(L-1,R):
            boxes[num] = work
    print(f'#{tc}',*boxes)
            

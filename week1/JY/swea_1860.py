T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arrivals = list(map(int,input().split()))

    # 오름차순(bubble sort)
    for i in range(N-1,-1,-1):
        for j in range(i):
            if arrivals[j] > arrivals[j+1] :
                arrivals[j], arrivals[j+1] = arrivals[j+1], arrivals[j]
    
    Possible = True

    for i in range(N):
        time = arrivals[i]
        bread = (time//M) * K
        customer = i + 1

        if bread - customer < 0:
            Possible = False
            break

    if Possible:
        print(f'#{tc}', "Possible")
    else:
         print(f'#{tc}', "Impossible")
def count_change(N):
    N= int(N)
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    counts = []
    for c in change:
        count = N // c
        counts.append(count)
        N %= c
    return counts
        

T = int(input())
for tc in range(1,T+1):
    money = input()
    result = count_change(money)
    print(f'#{tc}')
    print(*result)
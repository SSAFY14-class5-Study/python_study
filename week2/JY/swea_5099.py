from collections import deque

def find_last_pizza(cheese,N,M):
    oven = deque()
    nums = [i for i in range(1,M+1)]
    pizzas = list(zip(nums,cheese))

    for i in range(N):
        oven.append(pizzas.pop(0))
    
    while len(oven) > 1:
        num, amoun_of_cheese = oven.popleft()
        amoun_of_cheese //= 2

        if amoun_of_cheese == 0 and pizzas:
            oven.append(pizzas.pop(0))
        elif amoun_of_cheese > 0:
            oven.append((num, amoun_of_cheese))
    
    num, amoun_of_cheese = oven.popleft()

    return num
            


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    cheese = list(map(int,input().split()))
    ans = find_last_pizza(cheese,N,M)
    print(f'#{tc} {ans}')

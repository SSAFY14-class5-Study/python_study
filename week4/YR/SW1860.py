# 진기의 최고급 붕어빵

T = int(input())

for tc in range(1, T+1):

    N, M, K = map(int, input().split())

    people = list(map(int, input().split()))
    people.sort()

    valid = 'Possible'

    for i in range(N):
        x = people[i]

        breads = (x//M) * K

        if breads < i+1:
            valid = 'Impossible'
            break

    print(f"#{tc} {valid}")
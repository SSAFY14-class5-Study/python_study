from collections import deque

def encryptor(nums):
    q = deque(nums)

    while True:
        for step in range(1,6):
            data = q.popleft() - step
            if data <= 0:
                q.append(0)
                return list(q)
            q.append(data)

for tc in range(1,11):
    N = int(input())
    nums = list(map(int,input().split()))
    ans = encryptor(nums)
    print(f'#{tc}', *ans)
from collections import deque

def encryptor(data):
    code = deque(data)
    
    while True:
        for step in range(1,6):
            num = code.popleft() - step
            if num <= 0:
                code.append(0)
                return code
            else:
                code.append(num)


for tc in range(1,11):
    N = int(input())
    data = list(map(int,input().split()))
    ans = encryptor(data)
    print(f'#{tc}', *ans)
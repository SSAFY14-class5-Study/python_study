# 설탕 배달
N = int(input())

ans = 0

if N % 5 == 0:
    N //= 5
    ans += 1
    if N & 3 == 0:
        ans += 1
elif N % 3 == 0:
    N //= 3
    ans += 1
else:
    ans = -1

print(ans)
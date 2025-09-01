N = int(input())
num = N
cnt = 0

while True:
    cnt += 1
    a = num // 10        # 10의 자리
    b = num % 10         # 1의 자리
    c = (a + b) % 10     # 두 자리수 합의 1의 자리
    num = b * 10 + c     # 새 숫자 생성

    if num == N:         # 처음 숫자와 같으면 종료
        break

print(cnt)

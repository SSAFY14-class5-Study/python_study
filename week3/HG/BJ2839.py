# 설탕배달

N = int(input())

bag = 0
while N >= 0:  #
    if N % 5 == 0:
        bag += N // 5
        print(bag)
        break
    # 5로 나누어떨어지지 않으면 3kg 봉지 1개 사용
    N -= 3
    bag += 1
else: #While문도 else 쓸 수 있음..
    print(-1)

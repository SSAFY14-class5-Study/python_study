# [S/W 문제해결 기본] 7일차 - 암호생성기

for _ in range(10):
    tc = int(input())
    password = list(map(int, input().split()))

    while password[-1] != 0:
        # 1 ~ 5까지의 사이클을 돌며 숫자 감소
        for i in range(1, 6):
            new_pw = password[0] - i
            # 감소시켰을 때 음수가 되는 경우 0 반환
            if new_pw < 0:
                new_pw = 0
            password.append(new_pw)
            password.pop(0)

            # 마지막 숫자가 0이 되면 while문 종료
            if password[-1] == 0:
                break

    result = " ".join(map(str, password))
    print(f"#{tc} {result}")

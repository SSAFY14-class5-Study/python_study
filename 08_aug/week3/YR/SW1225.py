# 암호 생성기
for tc in range(1, 11):
    test_case = input()
    arr = list(map(int, input().split()))

    i = 1

    while True:
        x = arr.pop(0)
        x -= i

        if x <= 0:
            arr.append(0)
            break
        else:
            arr.append(x)

        i += 1
        if i > 5:
            i = 1

    print(f"#{test_case} ", *arr)
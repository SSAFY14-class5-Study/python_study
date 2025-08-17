# 농작물 수확하기

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # input값을 리스트에 넣기
    arr = []
    for _ in range(N):
        tmp_arr = list(map(int, input()))
        arr.append(tmp_arr)

    # 농작물 수확 : 우선 리스트에 마름모꼴 내부 값 저장
    income = []
    i = N // 2
    for r in range(N):
        income.append(arr[r][i : N - i])

        # 마름모 上
        if r < N // 2:
            i -= 1
        # 마름모 下
        else:
            i += 1

    # income 배열 돌면서 누적 값 산출
    cnt = 0
    for r in range(N):
        for i in range(len(income[r])):
            cnt += income[r][i]

    print(f"#{tc} {cnt}")

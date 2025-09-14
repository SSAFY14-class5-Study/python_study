# 9367. 점점 커지는 당근의 개수

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # N: 당근의 개수
    arr = list(map(int, input().split()))

    max_cnt = 1     # max_cnt: 연속하는 숫자 카운트(결과)
    cnt = 1         # cnt: 임시 카운트

    for i in range(N-1):
        # 당근의 크기가 연속으로 커지는 경우 cnt + 1
        if arr[i] < arr[i+1]:
            cnt += 1

        # 당근의 크기가 같거나 작다면
        elif arr[i] >= arr[i+1]:
            max_cnt = max(max_cnt, cnt)     # max값 갱신
            cnt = 1                         # cnt 초기화

    max_cnt = max(max_cnt, cnt)

    print(f'#{tc} {max_cnt}')
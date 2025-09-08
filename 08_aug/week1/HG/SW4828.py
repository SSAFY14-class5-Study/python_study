T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 정수 갯수(정수로 사용해야하니까 int 변환)
    num = list(map(int, input().split()))  # 각 정수 받음

    # 최댓값 초기화(인덱스)
    max_val = num[0]
    min_val = num[0]

    for i in range(
        1, N
    ):  # 1부터 시작? 이미 첫 번째 숫자를 기준(최댓값이자 최솟값)으로 사용했기 때문에
        # 최댓값 갱신
        if num[i] > max_val:
            max_val = num[i]
        # 최솟값 갱신
        if num[i] < min_val:
            min_val = num[i]
    # 주의 if 문 밖에서 선언
    result = max_val - min_val

    print(f"#{tc} {result}")

T = int(input())  # 테스트 케이스

for tc in range(1, T+1):
    N = int(input())  # 카드 장수
    numbers = list(map(int, input()))  # 공백 없이 숫자 입력

    arr = [0] * 10  # 0~9 카드 개수 저장
    max_count = -1  # 최대 빈도수
    max_card = -1   # 해당 카드 숫자

    for i in numbers:
        arr[i] += 1  # 카드 개수 세기

    for j in range(len(arr)):
        if arr[j] >= max_count:    # 빈도수 계산
            max_count = arr[j]
            max_card = j    # 해당 카드 숫자

    print(f"#{tc} {max_card} {max_count}")

# [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = int(input())

    # 0 ~ 9까지 각 인덱스에 누적값 넣을 빈 리스트 생성
    card_arr = [0] * 10
    for i in range(N):
        card_arr[num % 10] += 1  # N의 각 자릿수의 숫자마다 +!
        num //= 10  # 10으로 나눠서 1의 자릿수 삭제시키기 > 다시 반복

    # max값 가정
    max_value = card_arr[0]
    max_index = 0
    for i in range(1, len(card_arr)):
        if max_value <= card_arr[i]:
            max_value = card_arr[i]
            max_index = i

    print(f"#{tc} {max_index} {max_value}")

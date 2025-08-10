# [파이썬 S/W 문제해결 기본] 3일차 - 글자수

T = int(input())

for tc in range(1, T + 1):
    str_1 = list(map(str, input()))
    str_2 = list(map(str, input()))

    # 최댓값을 0으로 가정
    max_val = 0

    for i in range(len(str_1)):  # 첫 번째 문자열 순회
        cnt = 0
        for j in range(len(str_2)):  # 두 번째 문자열 순회
            if str_1[i] == str_2[j]:  # 그 두 문자가 같다면 cnt에 +1
                cnt += 1
        if max_val < cnt:
            max_val = cnt

    print(f"#{tc} {max_val}")

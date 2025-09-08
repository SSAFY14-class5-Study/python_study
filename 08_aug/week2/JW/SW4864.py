# [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

T = int(input())

for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())

    # 완전 탐색 함수 정의
    def brute_force(finding, arr):
        i = 0  # finding의 인덱스
        j = 0  # arr의 인덱스

        while j < len(finding) and i < len(arr):
            if arr[i] != finding[j]:  # 다른 글자를 만나면
                i = i - j  # i를 [비교시작점+1] 위치로 되돌림
                j = -1  # j는 0이 될 준비(뒤에서 j+1하기 때문)

            i = i + 1
            j = j + 1  # => 즉, j = 0

        if j == len(finding):  # finding이 끝까지 맞았다면
            return i - len(finding)  # 시작 인덱스 반환
        else:  # 못 찾았다면
            return -1

    result = brute_force(str1, str2)

    # 결과 출력
    if result == -1:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")

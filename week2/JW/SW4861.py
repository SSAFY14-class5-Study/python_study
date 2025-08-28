# [파이썬 S/W 문제해결 기본] 3일차 - 회문

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 문자열 리스트로 입력 받기
    arr = []
    for _ in range(N):
        temp_arr = list(input())
        arr.append(temp_arr)

    result = None

    # 가로 탐색
    for r in range(N):
        for c in range(N - M + 1):
            # 회문 검사할 단어 추출
            temp_text = list(arr[r][c : c + M])

            for i in range((M // 2) + 1):
                if temp_text[i] != temp_text[-1 - i]:
                    break  # 회문이 아니라면 중단
            else:  # 회문이라면 단어를 합치고(join) 멈춤
                result = "".join(temp_text)
                break

    # 세로 탐색
    if result == None:  # 가로 검색 후에도 none이라면
        for c in range(N):
            for r in range(N - M + 1):
                # 빈 리스트 생성
                temp_text = []

                for m in range(M):  # 회문 검사할 단어를 세로로 추출
                    temp_text.append(arr[r + m][c])

                for i in range((M // 2) + 1):
                    if temp_text[i] != temp_text[-1 - i]:
                        break  # 회문이 아니라면 중단
                else:  # 회문이라면 단어 조합(join)
                    result = "".join(temp_text)

    # 결과 출력
    print(f"#{tc} {result}")

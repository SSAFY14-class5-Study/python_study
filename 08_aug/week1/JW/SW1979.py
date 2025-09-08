# 어디에 단어가 들어갈 수 있을까

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    # 단어퍼즐 리스트 생성
    arr = []
    for _ in range(N):
        new_arr = list(map(int, input().split()))
        arr.append(new_arr)

    word_cnt = 0  # 결과(길이가 K인 단어가 들어갈 수 있는 자리) 누적값
    cnt = 0  # 단어퍼즐 리스트(arr)에서 1의 개수 세기

    # ex. 단어 길이가 3인 경우,
    # arr 리스트의 r, c를 순회하며 1이 있는 경우 cnt에 1을 더한다
    # 1을 더하다가 0 발견 시 cnt = 0으로 cnt값 리셋

    # 가로 탐색
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:  # 단어가 들어갈 수 있는 자리(1)인 경우
                cnt += 1  # cnt에 1 더한다

            elif arr[r][c] == 0:  # 단어가 들어갈 수 없는 자리(0)인 경우
                # 빈칸(1)이 연속으로 K개 있다면 = 단어가 들어갈 수 있는 자리
                if cnt == K:
                    word_cnt += 1  # 그러므로 결과 누적값에 +1
                cnt = 0  # 이후 cnt 값은 초기화

        # 가로 한 줄 다 돌았다면 => cnt가 목표값(K)에 도달했는 지 확인
        if cnt == K:
            word_cnt += 1  # 도달했다면 결과 누적값에 +1
        cnt = 0  # 이후 cnt값은 초기화

    # 세로 탐색
    for c in range(N):
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            elif arr[r][c] == 0:
                if cnt == K:
                    word_cnt += 1
                cnt = 0

        # 세로 한 줄 다 돌았다면 => cnt가 목표값(K)에 도달했는 지 확인
        if cnt == K:
            word_cnt += 1  # 도달했다면 결과 누적값에 +1
        cnt = 0  # 이후 cnt값은 초기화

    print(f"#{tc} {word_cnt}")

# 스도쿠 검증

T = int(input())

for tc in range(1, T + 1):

    # 비어있는 스도쿠 리스트에 숫자 채우기
    sudoku = []
    for _ in range(9):
        arr_column = list(map(int, input().split()))
        sudoku.append(arr_column)

    # 스도쿠 결과 감정할 변수(is_sudoku)를 일단 True로 가정
    is_sudoku = True

    # 가로
    for r in range(9):
        # 스도쿠 숫자별로 cnt 인덱스에 +1 되도록 하기
        # 가로 한 줄 돌고나서 cnt 리스트를 확인했을 때 인덱스 1 ~ 9까지 모두 '1'이면 통과(True)
        cnt = [0] * 10
        for c in range(9):
            cnt[sudoku[r][c]] += 1

        # cnt 리스트 검증
        for i in range(1, 10):
            if cnt[i] != 1:
                is_sudoku = False

    # 세로
    if is_sudoku == True:  # 가로가 모두 통과되었을 경우에만 세로 검증 시작
        for c in range(9):
            cnt = [0] * 10
            for r in range(9):
                cnt[sudoku[r][c]] += 1

            # cnt 리스트 검증
            for i in range(1, 10):
                if cnt[i] != 1:
                    is_sudoku = False

    # 3X3 격자
    if is_sudoku == True:  # 가로, 세로가 모두 통과되었을 경우에만 3x3 격자 검증 시작
        for R in range(0, 9, 3):
            for C in range(0, 9, 3):
                cnt = [0] * 10
                for r in range(3):
                    for c in range(3):
                        cnt[sudoku[R + r][C + c]] += 1

                for i in range(1, 10):
                    if cnt[i] != 1:
                        is_sudoku = False

    # 가로, 세로, 3x3격자 모두 통과하였다면 is_sudoku 결과값은 True
    if is_sudoku == True:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")

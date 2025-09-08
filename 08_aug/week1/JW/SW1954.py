# 달팽이 숫자

T = int(input())

for tc in range(1, T + 1):
    # 달팽이 배열 크기(size * size)
    size = int(input())

    # 기본값(0) 배열
    arr = []
    for _ in range(size):
        arr_column = [0] * size
        arr.append(arr_column)

    # 방향 델타값(우 > 하 > 좌 > 상)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 초기 시작 위치 및 값
    r = 0
    c = 0
    d = 0
    cnt = 1  # (0, 0)에 들어가는 숫자 = 1
    arr[r][c] = cnt

    # 이동하는 위치를 달팽이 배열 사이즈 내로 제한
    while cnt < size * size:
        # 위치 이동
        nr = r + dr[d]  # nr = new row
        nc = c + dc[d]  # nc = new column

        if 0 <= nr < size and 0 <= nc < size and arr[nr][nc] == 0:
            # nr은 범위 이내 and nc는 범위 이내 and 아직 기본값(0)인 가?
            cnt += 1
            arr[nr][nc] = cnt
            # r, c = nr, nc
            r = nr
            c = nc

        # 방향 인덱스 순환[ex. 현재 인덱스가 0인 경우 -> 다음 인덱스는 (0 + 1) % 4 = 1]
        else:
            d = (d + 1) % 4

    print(f"#{tc}")

    # row 출력
    for R_value in arr:
        # column 출력
        for C_value in R_value:
            print(C_value, end=" ")

        # column 한 줄 끝나면 줄 바꾸기
        print()

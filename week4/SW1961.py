# 숫자 배열 회전

T = int(input())


def rotate(arr):
    n_size = len(arr) #함수 안은 독립적인 변수 사용(N 사용x)
    new_arr = [[0] * n_size for _ in range(n_size)]
    for r in range(n_size):
        for c in range(n_size):
            new_arr[c][n_size - r - 1] = arr[r][c]
    return new_arr


for tc in range(1, T + 1):
    N = int(input())  #N 사용 가능
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_90 = rotate(arr) #함수 파라미터 넣어서 시계방향 90도씩 회전
    arr_180 = rotate(arr_90)
    arr_270 = rotate(arr_180)

    print(f"#{tc}") #출력 테케번호 1줄
    for i in range(N): #회전한 배열 1행 나열,2행 나열...
        s90 = "".join(map(str, arr_90[i])) # 주의 '' 공백 없이 문자열 붙여야함(행 1개 표현)
        s180 = "".join(map(str, arr_180[i]))
        s270 = "".join(map(str, arr_270[i]))

        print(f"{s90} {s180} {s270}") # 주의 배열 구분은 공백 필요

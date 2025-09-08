# 숫자 배열 회전

T = int(input())

for tc in range(1, T + 1):

    N = int(input())    # 배열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 생성

    result_90 = []
    result_180 = []
    result_270 = []

    # 출력
    print(f"#{tc}")

    # 90도
    for r in range(N):
        arr90 = ""
        for c in range(N-1, -1, -1):   # 행
            arr90 += str(arr[c][r])      # (c, r)
        # print(arr90)
        result_90.append(arr90)

    # 180도
    for r in range(N-1, -1, -1):
        arr180 = ""
        for c in range(N-1, -1, -1):
            arr180 += str(arr[r][c])
        # print(arr180)
        result_180.append(arr180)

    # 270도
    for r in range(N-1, -1, -1):
        arr270 = ""
        for c in range(N):
            arr270 += str(arr[c][r])
        # print(arr270)
        result_270.append(arr270)
    
    # 출력
    for i in range(N):
        print(result_90[i], result_180[i], result_270[i])
    
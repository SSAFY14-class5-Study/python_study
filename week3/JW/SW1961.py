# 1961. 숫자 배열 회전

T = int(input())

for tc in range(1, T+1):
    # N : 행렬(N*N)
    N = int(input())

    # arr : 테스트케이스를 입력 받을 리스트
    arr = []
    for _ in range(N):
        temp_arr = list(map(int, input().split()))
        arr.append(temp_arr)

    # < 회전 >
    # 90도 회전
    new_arr_90 = []
    for c in range(N):
        temp_arr = []
        for r in range(N-1, -1, -1):
            temp_arr.append(arr[r][c])
        new_arr_90.append(temp_arr)
        
    # 180도 회전
    new_arr_180 = []
    for r in range(N-1, -1, -1):
        temp_arr = []
        for c in range(N-1, -1, -1):
            temp_arr.append(arr[r][c])
        new_arr_180.append(temp_arr)

    # 270도 회전
    new_arr_270 = []
    for c in range(N-1, -1, -1):
        temp_arr = []
        for r in range(N):
            temp_arr.append(arr[r][c])
        new_arr_270.append(temp_arr)


    # 새 리스트에 회전한 값을 모두 삽입
    new_list = []
    new_list.append(new_arr_90)
    new_list.append(new_arr_180)
    new_list.append(new_arr_270)

    print(f'#{tc}')

    for r in range(N):
        lst = []
        for arr in new_list:
            lst.append("".join(map(str, arr[r])))
        result = " ".join(lst)
        print(result)
        
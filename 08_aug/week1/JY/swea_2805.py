def crops_harvest(field, N):
    harvest = 0    
    mid = N // 2

    for r in range(N):
        if r <= mid:
            span = r
        else:
            span = N - 1 -r
        
        start = mid - span
        end = mid + span
        
        for c in range(start, end +1):
            harvest += int(field[r][c])

    return harvest


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    field = [list(input())for _ in range(N)]
    ans = crops_harvest(field,N)
    print(f'#{tc} {ans}')


"""
arr = [[1, 4, 0, 5, 4],
       [4, 4, 2, 5, 0],
       [0, 2, 0, 3, 2],
       [5, 1, 2, 0, 4],
       [5, 2, 2, 1, 2]]

i = 2 # n// 2
for r in range(5):
    print(arr[r][0+i:5-i])

    if r >= 2:
        i += 1
    else:
        i -= 1
"""
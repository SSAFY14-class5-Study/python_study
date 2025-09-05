# 1215. [S/W 문제해결 기본] 3일차 - 회문1

for tc in range(1, 11):
    N = int(input())    # 회문의 길이

    arr = []
    for _ in range(8):
        temp = list(map(str, input()))
        arr.append(temp)

    cnt = 0
    # 가로 탐색
    for r in range(8):
        for c in range(0, 9-N):
            for i in range(N//2):
                if arr[r][c+i] != arr[r][c+N-1-i]:
                    break
            else:
                cnt += 1

    # 세로 탐색
    for c in range(8):
        for r in range(0, 9-N):
            for i in range(N//2):
                if arr[r+i][c] != arr[r+N-1-i][c]:
                    break
            else:
                cnt += 1

    print(f'#{tc} {cnt}')
    
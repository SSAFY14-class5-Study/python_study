# 색종이


paper = [list([0] * 100) for _ in range(100)]
cnt = 0

# 색종이크기 순회

N = int(input())
i = 0
while i < N:
    r, c = map(int, input().split())

    i += 1
    x = r
    while x < (r + 10):

        y = c
        while y < (c + 10):
            start_c = c
            if paper[x][y] == 0:
                paper[x][y] = 1
            y += 1
        x += 1


# 전체 배열 돌면서 cnt 계산
r = 0
while r < 100:
    c = 0
    while c < 100:
        if paper[r][c] == 1:
            cnt += 1
        c += 1
    r += 1

print(cnt)

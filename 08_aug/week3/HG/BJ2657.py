# 색종이-2

N = int(input())
paper = [([0] * 101) for _ in range(101)]  # 인덱스에러방지 +1

# 상 하 좌 우 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
i = 0
cnt = 0

while i < N:  # 색종이 수만큼 범위 체크해야함
    r, c = map(int, input().split())
    x = r
    # 행 순회
    while x < (r + 10):
        y = c
        # 열 순회
        while y < (c + 10):
            paper[x][y] = 1
            y += 1
        x += 1

    i += 1

# 델타 사용
x = 0
while x < 101:
    y = 0
    while y < 101:
        # 색칠된 칸일 경우에만 둘레 탐색
        if paper[x][y] == 1:

            # 색칠된 해당 칸의 상하좌우 탐색
            for i in range(4):
                nr = x + dr[i]
                nc = y + dc[i]
                # 경계 검사
                if nr < 0 or nr > 100 or nc < 0 or nc > 100:
                    cnt += 1
                elif paper[nr][nc] == 0:
                    cnt += 1
        y += 1
    x += 1
print(cnt)

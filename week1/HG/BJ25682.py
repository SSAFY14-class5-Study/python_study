N, M, K = map(int, input().split())
board = []
# 체스판은 2종류 : 흰색시작 , 검은색 시작
# 누적합을 구해두면, 어떤 k x k 영역의 비용총합도 계산 가능
for _ in range(N):
    board.append(input())

min_repaint = 2000

for r in range(N - K + 1):  # 잘라낼 kxk 보드의 시작점(r,c) 모두 순회
    for c in range(M - K + 1):  # 세로 M 기준

        repaint_w = 0  # 흰색시작 체스판 기준 비용(몇개 새로 칠해야하는지)
        repaint_b = 0  # 검은색 시작
        # (i+j)의 홀짝 여부로 기준색 결정(흰색시작인지, 검은색 시작인지)
        for i in range(K):  # KxK 영역 내부 순회
            for j in range(K):
                if (i + j) % 2 == 0:
                    if board[r + i][c + j] != "W":
                        repaint_w += 1
                    if board[r + i][c + j] != "B":
                        repaint_b += 1
                    else:  # 홀수칸 적용 내용
                        # 흰색 시작 체스판과 비교
                        if board[r + i][c + j] != "B":  # 홀수니까 반대
                            repaint_w += 1
                        if board[r + i][c + j] != "W":
                            repaint_b += 1
            crr_min = 0
            if repaint_w < repaint_b:
                crr_min = repaint_w
            else:
                crr_min = repaint_b

            if crr_min < min_repaint:
                min_repaint = crr_min

print(min_repaint)

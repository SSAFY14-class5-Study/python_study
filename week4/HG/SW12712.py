"""
SWEA 12712 - 파리퇴치3 (Python 풀이)

[문제 요약]
- N x N 격자에 파리 수가 들어있다.
- 살충 스프레이는 두 가지 모양으로 뿌릴 수 있다.
  1) 십자(+) 모양
  2) 대각선(X) 모양
- 중심 칸에서 시작하여 각 방향으로 (M-1)칸까지 영향을 준다.
- 한 번에 잡을 수 있는 파리 수(=합계)가 최대가 되도록 할 때, 그 최대값을 구한다.

[입력 형식]
- 첫 줄: 테스트 케이스 수 T
- 각 테스트 케이스마다:
  - 첫 줄: N M
  - 다음 N줄: 각 줄에 N개의 정수(격자 값)

[출력 형식]
- 각 테스트 케이스마다 "#t ans" 형태로 출력 (t는 1부터 시작하는 케이스 번호)

이 코드는 초보자분들을 위해 델타(이동) 배열과 for문(특히 중첩 for문)의 동작 방식을
주석으로 자세히 설명합니다.
"""

import sys


def in_range(x: int, y: int, n: int) -> bool:
    """좌표 (x, y)가 0 ~ n-1 범위 안에 있는지 확인하는 함수.

    - 격자 밖으로 나가면 IndexError 가 발생하므로, 더하기 전에 항상 범위를 체크합니다.
    """
    return 0 <= x < n and 0 <= y < n


def max_kill_with_sprays(board, n: int, m: int) -> int:
    """주어진 격자 board 에서 십자(+)와 대각선(X) 스프레이로 잡을 수 있는
    파리 수의 '최대값'을 계산해서 반환합니다.

    핵심 아이디어: 델타(이동) 배열과 중첩 for문
    - 델타 배열: 상하좌우/대각선 방향으로 한 칸 이동할 때 더할 좌표 변화를 미리 묶어 둔 것
    - 중첩 for문: 모든 칸을 중심으로 삼아, 각 방향으로 M-1칸씩 확장하며 합을 계산
    """

    # 델타(이동) 배열 설명
    # - 델타란? 어떤 칸 (x, y)에서 이웃한 칸으로 이동할 때 더해야 하는 (dx, dy)의 묶음입니다.
    # - 예: 위로 한 칸은 (dx, dy) = (-1, 0), 오른쪽 한 칸은 (0, +1)
    # - 이런 방향 묶음을 리스트로 만들어 놓고, for문으로 반복하며 좌표를 더해 나갑니다.

    # 십자(+) 모양: 상, 하, 좌, 우 4방향
    plus_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 대각선(X) 모양: 좌상, 우상, 좌하, 우하 4방향
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    best = 0  # 지금까지 찾은 최대 파리 수

    # 중첩 for문의 원리
    # - 바깥 for: 격자의 모든 행 x 를 차례대로 고른다.
    # - 그 안쪽 for: 각 행에 대해 모든 열 y 를 차례대로 고른다.
    #   => 이렇게 하면 (x, y) 모든 칸을 정확히 한 번씩 방문합니다.
    for x in range(n):  # 행을 0 ~ n-1 까지 돈다
        for y in range(n):  # 열을 0 ~ n-1 까지 돈다
            # 1) 십자(+) 모양 합 계산
            cross_sum = board[x][y]  # 중심 칸 포함

            # 깊은(여러 겹) for문이 필요한 이유
            # - 각 칸 (x, y)를 중심으로 4방향을 모두 시도해야 하고,
            # - 각 방향으로 1 ~ M-1 칸까지 확장해야 하므로
            #   "방향을 도는 for" 내부에 "거리(스텝)를 도는 for"를 또 넣습니다.
            for dx, dy in plus_dirs:  # 4개 방향 반복
                for step in range(1, m):  # 1칸, 2칸, ... (M-1)칸까지 확장
                    nx, ny = x + dx * step, y + dy * step
                    if not in_range(nx, ny, n):  # 격자 밖이면 그 방향은 중단
                        break
                    cross_sum += board[nx][ny]

            # 2) 대각선(X) 모양 합 계산
            diag_sum = board[x][y]  # 중심 칸 포함
            for dx, dy in diag_dirs:
                for step in range(1, m):
                    nx, ny = x + dx * step, y + dy * step
                    if not in_range(nx, ny, n):
                        break
                    diag_sum += board[nx][ny]

            # 현재 칸을 중심으로 한 두 모양 중 더 큰 값을 고려
            best = max(best, cross_sum, diag_sum)

    return best


def solve() -> None:
    input = sys.stdin.readline
    T = int(input().strip())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(N)]

        ans = max_kill_with_sprays(board, N, M)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    # 예시 실행 방법 (터미널):
    # python3 week4/SW12712.py < input.txt
    #
    # input.txt 예시
    # 2
    # 5 2
    # 1 3 3 6 7
    # 8 13 9 12 8
    # 4 16 11 12 6
    # 2 4 1 23 2
    # 9 13 4 7 3
    # 6 3
    # 1 1 1 1 1 1
    # 1 1 1 1 1 1
    # 1 1 1 1 1 1
    # 1 1 1 1 1 1
    # 1 1 1 1 1 1
    # 1 1 1 1 1 1
    solve()


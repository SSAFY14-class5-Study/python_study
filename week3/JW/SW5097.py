# [파이썬 S/W 문제해결 기본] 6일차 - 회전

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N : 숫자 갯수
    # M : 뒤로 보내는 횟수

    lst = list(map(int, input().split()))

    # 0번째 인덱스 숫자를 새로 추가하고(뒤에 삽입) 0번 인덱스 삭제(pop)
    for _ in range(M):
        lst.append(lst[0])
        lst.pop(0)

    print(f"#{tc} {lst[0]}")

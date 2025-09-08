# [S/W 문제해결 기본] 1일차 - View

T = 10
for tc in range(1, T + 1):
    N = int(input())  # 건물 개수
    buildings = list(map(int, input().split()))  # 빌딩 높이
    total = 0  # 조망권 확보된 세대 수

    # 양 옆 두 칸은 건물이 없으므로 범위 : 2 ~ N-2
    for i in range(2, N - 2):
        # Max 함수 사용하지 않고 max_v 구하기
        max_v = buildings[i - 2]  # max_v의 기본값 구하기
        for j in [i - 1, i + 1, i + 2]:
            if max_v < buildings[j]:
                max_v = buildings[j]

        # 각 빌딩별로 돌아가며 max_v값과 비교
        if buildings[i] > max_v:
            # view = 건물 높이에서 조망권 획득한 세대 수를 total에 합산
            view = buildings[i] - max_v
            total += view

        # Max 함수 사용한 경우
        #  if buildings[i] > max(
        #     buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2]
        # ):
        #     view = buildings[i] - max(
        #         buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2]
        #     )
        #     total += view

    print(f"#{tc} {total}")

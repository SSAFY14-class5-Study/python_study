# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    # 각 플레이어별로 빈 리스트를 생성 
    #  -> 가져온 카드 숫자를 인덱스로 사용
    player_1 = [0] * 12   # i ~ i+2번째까지 비교해야하므로 넉넉하게 * 12
    player_2 = [0] * 12
    result = 0  # 기본값(무승부 : 0)

    for i in range(len(arr)):
        # 카드 배부
        if i % 2 == 0:
            player_1[arr[i]] += 1
        else:
            player_2[arr[i]] += 1
        
        # 플레이어 1
        for idx in range(10):
            # run
            if player_1[idx] > 0 and player_1[idx+1] > 0 and player_1[idx+2] > 0:
                result = 1
                break
            # triplet
            elif player_1[idx] == 3:
                result = 1
                break
        # 승자가 결정되면 중단
        if result:
            break

        # 플레이어 2
        for idx in range(10):
            # run
            if player_2[idx] > 0 and player_2[idx+1] > 0 and player_2[idx+2] > 0:
                result = 2
                break
            # triplet
            elif player_2[idx] == 3:
                result = 2
                break
        # 승자가 결정되면 중단
        if result:
            break

    print(f'#{tc} {result}')
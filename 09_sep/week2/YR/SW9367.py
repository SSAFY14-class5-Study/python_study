# 점점 커지는 당근의 개수
T = int(input())

for tc in range(1, T+1):    # 테스트 케이스
    N = int(input())        # 당근의 개수
    carrots = list(map(int, input().split()))   # 당근 수확

    cnt = 1     # 당근 개수
    mx_cnt = 0  # 최댓값 비교

    for i in range(N-1):
        if carrots[i+1] > carrots[i]:
            cnt += 1 
        else:   # 연속 판별
            cnt = 1
        
        if mx_cnt < cnt:
            mx_cnt = cnt
    # 출력
    print(f"#{tc} {mx_cnt}")   
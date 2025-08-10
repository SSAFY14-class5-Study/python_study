# View
for tc in range(1, 11): # 10개의 테스트 케이스
    N = int(input())    # 건물 개수
    heights = list(map(int, input().split()))   # 건물 높이

    cnt = 0     # 조망권 확보 세대 수
    for i in range(2, N-2):     # 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0
        left = max(heights[i-1], heights[i-2])      # 기준점 왼쪽 건물
        right = max(heights[i+1], heights[i+2])     # 기준점 오른쪽 건물

        if heights[i] > left and heights[i] > right: # 기준점이 제일 크다면
            cnt += heights[i] - max(left, right)    # 조망권 확보 세대 더하기
    # 출력
    print(f"#{tc} {cnt}")
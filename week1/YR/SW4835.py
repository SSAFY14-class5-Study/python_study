T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    N, M = map(int, input().split())    # 정수 개수 N, 구간 개수 M
    arr = list(map(int, input().split()))  # 정수 입력

    max_v = 0   # 최댓값 비교 변수
    min_v = float('inf')  # 최소값 비교 변수 (여기서 float('inf')는 무한대)

    for i in range(N - M + 1):  # N=5, M=3이라면 3개 생김
        sum_num = sum(arr[i:i+M])   # 구간합 더하기
    
        if sum_num > max_v:     # 최대값 구하기
            max_v = sum_num
        
        if sum_num < min_v:     # 최소값 구하기
            min_v = sum_num

    # 출력
    print(f"#{tc} {max_v-min_v}")
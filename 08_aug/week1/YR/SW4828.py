# minmax
T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    N = int(input())    # 양수의 개수
    numbers = list(map(int, input().split()))   # 양수 입력

    max_v = 0       # 최대값 비교 변수
    min_v = float('inf')    # 최소값 비교 변수

    for i in range(len(numbers)):
        if numbers[i] > max_v:      # 최대값 찾기
            max_v = numbers[i]

        if numbers[i] < min_v:      # 최소값 찾기
            min_v = numbers[i]
        
    # 출력
    print(f"#{tc} {max_v - min_v}")
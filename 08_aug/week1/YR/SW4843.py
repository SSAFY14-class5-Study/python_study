# 특별한 정렬
# 함수 오름차순 정렬 (버블 사용)
def bubble_sort(arr):
    N = len(arr)
    for i in range(N-1):
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 함수 적용 및 복사
    sorted_arr = bubble_sort(numbers[:])

    result = []
    left = 0    # 처음 인덱스 (최소)
    right = N - 1   # 맨 끝 인덱스 (최대)

    while len(result) < 10 and left <= right:       # 종료조건
        result.append(sorted_arr[right])
        right -= 1      # 끝에서부터

        if len(result) < 10:
            result.append(sorted_arr[left])
            left += 1      # 시작부터


    # 출력
    print(f"#{tc}", *result)
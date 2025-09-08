# 숫자를 정렬하자
# 오름차순 정렬
def select_sort(arr, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
 
    return arr
 
T = int(input())    # 테스트 케이스
 
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 함수 적용 및 복사
    sorted_numbers = select_sort(numbers, N)
 
    # 출력
    print(f"#{tc}", *sorted_numbers)
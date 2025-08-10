# 숫자를 정렬하자


# 버블정렬 함수 정의
def bubble_sort(arr, n):
    for i in range(n - 1, 0, -1):  # 순서 : 뒤 > 앞
        for j in range(i):
            if arr[j] > arr[j + 1]:  # 나(j)보다 오른쪽(j+1)이 더 크면 둘이 자리 바꾸기
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    results = bubble_sort(num_list, N)

    print(f"#{tc}", *results)

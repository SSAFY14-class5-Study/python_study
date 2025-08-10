# [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    # 전체 페이지 수가 담긴 리스트 생성
    page_list = []
    for i in range(1, P + 1):
        page_list.append(i)

    # 이진 탐색 함수 정의
    def binarySearch(
        arr, N, key
    ):  # arr:페이지 리스트, N:총 페이지 수, key:찾으려는 페이지
        left = 0
        right = N - 1
        cnt = 0  # key를 찾는 데까지 걸린 횟수
        while left <= right:
            middle = (left + right) // 2
            cnt += 1

            if arr[middle] == key:  # key값을 찾으면 cnt 반환
                return cnt
            elif arr[middle] > key:
                right = middle
            else:
                left = middle
        return -1  # 찾는 값이 없을 때(실패 시)

    search_A = binarySearch(page_list, P, Pa)
    search_B = binarySearch(page_list, P, Pb)

    if search_A < search_B:
        print(f"#{tc} A")
    elif search_A == search_B:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} B")

# [파이썬 S/W 문제해결 기본] 1일차 - min max

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # 버블정렬 함수 생성
    def bubble_sort(num_list, N):
        for i in range(N - 1, 0, -1):  # 순서 : 뒤부터 앞으로
            for j in range(i):
                # j번째 값이 j+i값보다 크면 두 값위 위치를 바꾼다
                if num_list[j] > num_list[j + i]:
                    num_list[j] = num_list[j + i]
                    num_list[j + i] = num_list[j]
        return num_list

    # 버블 정렬시킨 새로운 리스트 생성
    new_list = bubble_sort(num_list, N)

    min_value = new_list[0]  # 리스트 가장 앞이 최소값
    max_value = new_list[-1]  # 리스트 마지막이 최대값

    print(f"#{tc} {max_value - min_value}")

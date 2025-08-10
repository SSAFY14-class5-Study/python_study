# 백만 개의 정수 정렬


# 카운팅 정렬 함수 생성
def counting_sort(data, k):
    # 0으로 채워진 리스트 생성
    # data의 각 값에 해당하는 인덱스에 해당 숫자의 개수만큼 누적시킬 리스트
    counts = [0] * (k - 1)
    temp = [0] * len(data)  # temp: data의 value를 정렬시켜 입력할 리스트

    # data 리스트에 있는 숫자(ex. 3)에 해당하는 counts의 인덱스 값(counts[3])에 +1
    for i in range(len(data)):
        counts[data[i]] += 1  # 발생 횟수 카운트

    for i in range(1, k + 1):
        counts[i] += counts[i - 1]  # 누적 횟수 계산

    # 누적합 배열(counts)을 뒤에서부터 앞으로 순회하면서 -1하면서 하나씩 숫자를 집어넣는다
    for i in range(len(data) - 1, -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]

    return temp


# input값을 num_list에 추가
num_list = list(map(int, input().split()))
arr = counting_sort(num_list, 1000000)
print(arr[500000])

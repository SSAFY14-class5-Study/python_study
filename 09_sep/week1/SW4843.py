# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))   # 배열 입력받을 때 정렬하기

    # 결과를 저장할 리스트 생성
    result = []

    while len(result) < 10:
        if len(result)%2 == 0:   # 인덱스의 나머지가 0인 경우 : 큰 수부터 넣기
            result.append(arr.pop())
        else:   # 인덱스의 나머지가 1인 경우 : 작은 수부터 넣기
            result.append(arr.pop(0))
        if len(arr) == 0:
            break

    print(f'#{tc}', ' '.join(map(str, result)))
    
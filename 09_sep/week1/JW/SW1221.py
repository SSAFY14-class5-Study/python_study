# 1221. [S/W 문제해결 기본] 5일차 - GNS

num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for tc in range(1, T+1):
    _, N = map(str, input().split())
    # _ : tc 번호 => 버리기
    # N : tc 길이

    N = int(N)
    arr = list(map(str, input().split()))

    # 입력 받은 배열(arr)을 숫자로 변환 후 오름차순으로 정렬하기
    for i in range(N):
        for idx in range(10):
            if arr[i] == num[idx]:
                arr[i] = idx
    arr.sort()

    # 외계 행성의 언어로 번역
    for i in range(N):
        arr[i] = num[arr[i]]

    print(f'#{tc}')
    print(' '.join(arr))

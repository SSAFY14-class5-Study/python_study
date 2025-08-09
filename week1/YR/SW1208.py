for i in range(1, 11):  
    dump = int(input())
    arr = list(map(int, input().split()))
    
    for _ in range(dump):
        # 최댓값, 최소값
        max_v = max(arr)
        min_v = min(arr)

        # 최대, 최소값의 인덱스 찾기 (덤프하려면 인덱스 알아야함)
        maxIdx = arr.index(max_v)
        minIdx = arr.index(min_v)

        # 덤프 수행
        arr[maxIdx] -= 1
        arr[minIdx] += 1

    result = max(arr) - min(arr)
    print(f"#{i} {result}")

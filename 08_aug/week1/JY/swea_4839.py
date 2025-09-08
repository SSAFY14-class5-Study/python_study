def binary_search(page,target):
    low = 1
    high = page
    count = 0

    while low <= high:
        mid = int((low + high)/2)

        if mid == target:
           return count
        elif mid < target:
            low = mid + 1
            count += 1
        else:
            high = mid - 1
            count += 1


T = int(input())
for tc in range(1,T+1):
    P,A,B = map(int,input().split())
    countA = binary_search(P,A)
    countB = binary_search(P,B)
    if countA < countB:
        print(f'#{tc}',"A")
    elif countB < countA:
        print(f'#{tc}',"B")
    else:
        print(f'#{tc}',0)

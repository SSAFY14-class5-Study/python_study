def is_increasing(nums):
    s = str(nums)

    for i in range(1,len(s)):
        if s[i] < s[i-1]:
            return False
    return True


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))

    max_val = -1
    for i in range(N):
        for j in range(i+1,N):
            prod = nums[i] * nums[j]
            if is_increasing(prod):
                if prod > max_val:
                    max_val = prod
    print(f'#{tc} {max_val}')

    
   
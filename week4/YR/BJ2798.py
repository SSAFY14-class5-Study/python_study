# 블랙잭

N, M = map(int, input().split())

number = list(map(int,input().split()))

max_v = 0
sum_v = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_v = number[i] + number[j] + number[k]

            if sum_v > M:
                continue
            else:
                if max_v < sum_v:
                    max_v = sum_v

print(max_v)        


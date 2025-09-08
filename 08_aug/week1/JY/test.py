arr = [0, 0, 1, 1, 1,1, 0, 0, 1, 1, 1, 1]


N = len(arr)

K = 4
cnt = 0
for i in range(N):
    if arr[i] == 1:
        cnt += 1
        
    else: # 연속된 1이 끊기고 0이 나옴
        if cnt == K:
            print("K!")

        cnt = 0
    
    print(i, arr[i], cnt)

if cnt == K:
    print("K!")

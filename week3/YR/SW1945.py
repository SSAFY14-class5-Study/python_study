# SWEA 1945. 간단한 소인수분해

T = int(input())

num = [2, 3, 5, 7, 11]

for tc in range(1, T + 1):
    N = int(input())

    arr = [0, 0, 0, 0, 0]   # 2, 3, 5, 7, 11

    i = 0   
    while i < len(num):     
        while N % num[i] == 0:
            N //= num[i]
            arr[i] += 1                  
        i += 1              

    # 출력
    print(f"#{tc} {arr[0]} {arr[1]} {arr[2]} {arr[3]} {arr[4]}")

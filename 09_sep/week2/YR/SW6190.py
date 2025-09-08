# 정곤이의 단조 증가하는 수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    result = []  
    for i in range(N-1):
        for j in range(i+1, N):
            num = N_list[i] * N_list[j]
            s = str(num)

            ok = True
            for k in range(1, len(s)):
                if s[k-1] > s[k]:   
                    ok = False
                    break

            if ok:
                result.append(num)  

    ans = max(result) if result else -1
    print(f"#{tc} {ans}")

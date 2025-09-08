# 부분집합의 합
T = int(input())    # 테스트케이스
 
A = [i for i in range(1,13)]  # 집합 A
subset = [[] for _ in range(2**12)] # 집합 A의 부분집합
 
# 비트 연산으로 부분집합을 생성하는 방법
n = len(A)
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            subset[i].append(A[j])
 
for tc in range(1, T+1):
    N, K = map(int, input().split())
 
    cnt = 0
    for i in range(len(subset)):
        if len(subset[i]) == N and sum(subset[i]) == K:
            cnt += 1    
 
 
    # 출력
    print(f"#{tc} {cnt}")
# 삼성시의 버스 노선
T = int(input())

for tc in range(1, T+1):
    N = int(input())        # 버스 노선

    A, B = [], []
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        A.append(Ai)
        B.append(Bi)
    
    P = int(input())
    C =[]
    for _ in range(P):
        num = int(input()) 
        C.append(num)

    arr = [0] * 5001

    for i in range(N):
        for j in range(A[i], B[i] + 1):
            arr[j] += 1


    result = []
    for k in C:
        result.append(arr[k])

    print(f"#{tc}", *result)
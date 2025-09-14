# 20551. 증가하는 사탕 수열

T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    result = 0  

    # B상지의 사탕 개수가 C보다 작아질 때까지 사탕 감소
    while B >= C:
        B -= 1
        result += 1

        if B == 0:  # 조건을 만족시킬 수 없다면 '-1' 출력
            result = -1
            break

    # A상지의 사탕 개수가 B보다 작아질 때까지 사탕 감소
    if result != -1:
        while A >= B:
            A -= 1
            result += 1

            if A == 0:  # 조건을 만족시킬 수 없다면 '-1' 출력
                result = -1
                break

    print(A, B, C)
    print(f'#{tc} {result}')
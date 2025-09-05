# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

T = int(input())

# 2진수 변환 함수
def binary(num):
    share = num // 2    # 몫
    rest = num % 2      # 나머지
    # num이 더 이상 나눌 수 없는 0, 1이 된 경우 그 값을 반환
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    return binary(share) + str(rest)


for tc in range(1, T+1):
    N, num_16 = map(str, input().split())
    N = int(N)
    
    ans = ""
    for i in range(N):
        char = num_16[i]   # char = 16진수 한자리
        if '0' <= char <= '9':  # 숫자일 때
            num_10 = ord(char) - ord('0')
        else:   # 알파벳일 때(A=10, B=11, ...)
            num_10 = ord(char) - ord('A') + 10
        result = binary(num_10)

        while len(result) < 4:
            result = "0" + result
        
        ans += result

    print(f'#{tc} {ans}')
    
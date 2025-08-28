# DP의 종류 : 2가지
# - memoization : 재귀함수 호출 + 재귀함수의 값 기억해두기 
# - tabulation : 반복문으로 풀이, dp table(배열, 리스트)를 먼저 생성, 작은 문제의 해를 구한 후 반복ㅈ

# f(10) = 1
# f(20) = 3
# f(30) = 5
 # f(30) = f(20) + f(10) *2

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    dp = [0] * 301
    dp[10] = 1
    dp[20] = 3
    dp [30] = 5

    for i in range(40, N+1):
        dp[i] = dp[i-10] + dp[i -20] * 2

    print(f'#{tc} {dp[N]}')


    



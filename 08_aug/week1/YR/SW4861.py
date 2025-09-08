# 회문
# 팰린드롬 함수
def palin(arr, N, M):
 
    # 가로 검사
    for r in range(N):
        row = arr[r]
         
        for c in range(N-M+1):
            word = row[c: c+M]
             
            if word == word[::-1]:  # 회문이면
                return word
 
    # 세로 검사
    for c in range(N):
        column = ""     # 열 저장 변수
         
        for r in range(N):
            column += arr[r][c]
 
        for r in range(N-M+1):
            word = column[r: r+M]

            if word == word[::-1]:
                return word
 
 
T = int(input())    # 테스트 케이스
for tc in range(1, T+1):
    N, M = map(int, input().split())
 
    array = [input() for _ in range(N)]
    
    find_word = palin(array, N, M)
 
    # 출력
    print(f"#{tc} {find_word}")
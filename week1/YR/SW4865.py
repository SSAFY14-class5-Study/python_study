# 글자수
T = int(input())    # 테스트 케이스
 
for tc in range(1, T+1):
    N = input()     # str1
    M = input()     # str2
 
    max_cnt = 0     # 문자 등장 횟수
    for char in N:
        cnt = M.count(char)
         
        if cnt > max_cnt:
            max_cnt = cnt
 
    # 출력
    print(f"#{tc} {max_cnt}")
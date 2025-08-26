# 공과 잡초
T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    S = input()     # 문자열
    cnt = 0
    
    i = 0
    while i < len(S):
        if S[i] == '(':
            if S[i+1] == ')':
                cnt += 1
            elif S[i+1] == '|':
                cnt += 1
        elif S[i] == ')':
            if S[i-1] == '(':
                cnt += 1

        i += 1


    # 출력
    print(f"#{tc} {cnt}")
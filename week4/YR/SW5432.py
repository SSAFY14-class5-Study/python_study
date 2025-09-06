# 쇠막대기 자르기
# 스택 괄호검사 사용

T = int(input())

for tc in range(1, T+1):    # 테스트 케이스

    arr = list(input().strip())
    
    iron = []   # 쇠막대기 검사
    cnt = 0     # 잘린 쇠막대기 수

    for i in range(len(arr)):
        if arr[i] == '(':
            iron.append('(')
        else:
            iron.pop()
            if arr[i-1] == '(':
                cnt += len(iron)        # [(, ( ,(...]
            else:
                cnt += 1        # 막대 끝이라 잘라봤자 1개

    # 출력
    print(f"#{tc} {cnt}")


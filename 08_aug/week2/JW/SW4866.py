# [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사


# 괄호 검사 함수 정의
def checking_par(str):
    stack = []  # 빈 스택 생성
    result = None  # 결과값으 임시로 설정

    for i in str:
        if i in ["(", "{"]:  # 여는 괄호가 나오면 스택에 추가
            stack.append(i)

        if len(stack) != 0:  # 스택이 비어있지 않다면(즉, 값이 있다면)
            # 소괄호 검증
            if i == ")":  # 닫는 소괄호가 나오면
                if stack[-1] != "(":  # 최신 스택이 여는 소괄호가 아니라면
                    result = 0  # 짝()이 아니므로 결과는 0
                    break

                else:  # 스택 값은 '('이고, i는 ')'인 경우
                    stack.pop()
                    result = 1

            # 중괄호 검증
            elif i == "}":  # 닫는 중괄호가 나오면
                if stack[-1] != "{":  # 최신 스택이 여는 중괄호가 아니라면
                    result = 0  # 짝{}이 아니므로 결과는 0
                    break
                else:  # 스택 값은 '{'이고, i는 '}'인 경우
                    stack.pop()
                    result = 1

        # 스택에 값이 없는 경우
        else:
            if i in [")", "}"]:  # 닫는 괄호가 나오면
                result = 0
                # break : 브레이크 걸 필요 없음
                return result

    if stack:  # 스택에 값이 남아있다면
        result = 0
    else:  # 값이 남아있지 않다면
        result = 1
    return result


# 데이터 입력
T = int(input())

for tc in range(1, T + 1):
    text = input()

    ans = checking_par(text)
    print(f"#{tc} {ans}")

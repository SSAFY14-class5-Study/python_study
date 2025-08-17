# [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

T = int(input())

for tc in range(1, T + 1):
    text = input()

    # pop 함수 정의
    def my_pop(str):
        stack = []  # 비어있는 스택 리스트 생성
        for i in str:
            if stack and stack[-1] == i:
                # 스택의 최신요소와 i가 같다면 pop
                stack.pop()
            else:
                stack.append(i)
        return len(stack)

    # 결과 출력
    result = my_pop(text)
    print(f"#{tc} {result}")

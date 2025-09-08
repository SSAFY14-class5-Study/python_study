# 그대로 출력하기

while True:
    try:  # try-except 문으로 더이상 입력 없으면 EOFError 처리
        line = input()

        print(line)

    except EOFError:
        break

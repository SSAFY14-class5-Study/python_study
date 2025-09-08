# 초심자의 회문 검사

T = int(input())

for tc in range(1, T + 1):
    word = list(input())
    print(word)

    for i in range(len(word)):
        # i번째 문자열이 뒤에서 i번째 문자열과 같은 지 확인
        if word[i] == word[-1 * (i + 1)]:
            result = 1
        else:
            result = 0

    print(f"#{tc} {result}")

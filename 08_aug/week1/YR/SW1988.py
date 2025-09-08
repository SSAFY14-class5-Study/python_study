# 초심자의 회문 검사
T = int(input())    # 테스트 케이스

for tc in range(1, T+1):
    str = input()

    if str == str[::-1]:    # 회문이면
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")


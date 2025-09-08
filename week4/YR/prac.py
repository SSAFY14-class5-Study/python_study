# 쇠막대기 자르기

T = int(input())

for tc in range(1, T+1):

    arr = list(input().strip())

    iron = []       # 검사에 이용할 배열
    stick = 0       # 막대의 개수
    cnt = 0         # 자른 막대의 개수

    for i in range(len(arr)):
        if arr[i] == '(':
            iron.append('(')

            if arr[i+1] == ')':
                cnt += len(iron)
        else:
            iron.pop()

            if arr[i-1] == '(':
                cnt += len(iron)
            else:
                stick -= 1
                cnt += stick
                cnt += 1
    # 출력
    print(f"#{tc} {cnt}")

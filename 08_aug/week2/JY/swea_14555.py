def find_minimum_ball(str):
    count = 0

    str = list(str)
    for i in range(len(str) - 1):
        if str[i] == '(' and str[i+1] != ')':
            count += 1
        elif str[i] != '(' and str[i+1] == ')':
            count += 1
        elif str[i] == '(' and str[i+1] ==')':
            count += 1
    return count


T = int(input())
for tc in range(1,T+1):
    str = input()
    ans = find_minimum_ball(str)
    print(f'#{tc} {ans}')
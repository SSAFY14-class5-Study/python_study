def check_matching_pair(line):
    stack =[]

    for ch in line:
        if ch == '(' or ch =='{':
            stack.append(ch)
        elif ch ==')' or ch =='}':
            if not stack:
                return 0
            top = stack.pop()
            if ch == ')' and top != '(':
                return 0
            if ch == '}' and top != '{':
                return 0
    
    if not stack:
        return 1
    return 0

T = int(input())
for tc in range(1,T+1):
    line = input()
    ans = check_matching_pair(line)
    print(f'#{tc} {ans}')
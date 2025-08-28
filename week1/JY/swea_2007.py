def pattern(string):
    for i in range(1,11):
        if string[:i] == string[i: i*2]:
            return i

T = int(input())
for tc in range(1,T+1):
    string = input()
    ans = pattern(string)
    print(f'#{tc} {ans}')
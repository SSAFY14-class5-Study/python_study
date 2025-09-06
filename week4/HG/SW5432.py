#쇠막대기 자르기

T = int(input())

for tc in range(1,T+1):
    arr = input()

    result = 0 #쇠막대기 개수
    sticks = 0 # 현재 놓여있는 쇠막대기 개수 저장(스택 역할)

    for i, char in enumerate(arr): #enumerate: 인덱스와 char 를 가져옴
        if char == '(':
            sticks +=1

        else:
            #쇠막대기가 끝나는 경우, 레이저가 발사되는 시점
            sticks-=1

            if arr[i-1] == '(': #바로 이전문자가 '('인 경우 : 레이저
                answer +=sticks 

            else: # arr[i-1] == ')'
                result +=1

print(f'#{tc} {result}')
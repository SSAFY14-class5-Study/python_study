# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 가로 길이 리스트 생성
    width = [0] * 301

    # 가로가 10, 20, 30일 때 종이를 붙일 수 있는 경우의 수를 저장
    width[10] = 1
    width[20] = 3
    width[30] = 5

    # 가로 길이별로 경우의 수 저장
    for i in range(40, N + 1):
        width[i] = width[i-10] + width[i-20] * 2
    
    print(f'#{tc} {width[N]}')
    
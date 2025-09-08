# 문자열 반복
T = int(input())

for tc in range(1, T + 1):
    R, S = input().split()  # R : 반복횟수, S: 문자열
    for i in S:
        print(int(R) * i, end="")
    print() #테스트케이스가 끝날때마다 줄바꿈 해줌
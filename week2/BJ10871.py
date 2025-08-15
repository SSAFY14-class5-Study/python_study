# X보다 작은수

N, X = map(int, input().split())
num = list(map(int, input().split()))  # 입력 1회 받으니까 반복문 밖에


for i in num:
    if i < X:
        print(i, end=" ")

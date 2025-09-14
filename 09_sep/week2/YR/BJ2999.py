# 비밀 이메일
msg = input()
N = len(msg)

divisor = []    # 약수 리스트

# 약수 리스트 구하기
for i in range(1, N + 1):
    if N % i == 0:
        divisor.append(i)

# R, C 값 구하기
if len(divisor) % 2 == 0:
    R = divisor[(len(divisor) // 2) -1]
    C = divisor[(len(divisor) // 2)]
else:
    R = C = divisor[(len(divisor) // 2)]

# 행렬 만들기
arr = []
idx = 0
for i in range(C):
    column = [0] * R
    for j in range(R):
        column[j] = msg[idx]
        idx += 1
    arr.append(column)

for i in range(R):
    for j in range(C):
        print(arr[j][i], end = '')
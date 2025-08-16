# 숫자의 합

N = int(input())
numbers = list(map(int, input())) #공백없이 문자열이니까 반복문으로 입력받기x, int 변환
sum = 0
for num in numbers:
    sum += num # 위에서 int변환했으니 여기서는 안해도 됨

print(sum)
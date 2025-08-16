# 평균
#O(N)

N = int(input())  # 시험과목 개수
grade = list(map(int, input().split()))
M = max(grade) #점수 중 최댓값

sum = 0
for num in grade:
    num = num/M*100
    sum += num

result = sum / N

print(result)

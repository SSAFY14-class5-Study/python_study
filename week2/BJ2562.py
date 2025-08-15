#최댓값
# 시간복잡도 : O(N)
max_v = 0 #값을 인덱스 말고 정수로 표현하면 인덱스값을 i로 가져갈 수 있음
max_idx = 0

for i in range(1, 10): # i 1부터 시작하면 max_idx 와 동일하게 카운트됨
    num = int(input())
    if num > max_v:
        max_v = num
        max_idx = i

print(max_v)
print(max_idx)

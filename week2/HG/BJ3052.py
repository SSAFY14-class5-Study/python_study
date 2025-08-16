# 나머지
# 시간복잡도 : O(1)
arr = []
remain = []
for i in range(1,11): #문제에서 주어진대로 1부터 10
    N = int(input())
    arr.append(N)
    
for num in arr: # 배열의 모든 요소 비교할땐 이렇게
    a = num % 42
    remain.append(a)
    b = set(remain) #중복제거해서 {}로 뱉음

print(len(b))
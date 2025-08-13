#영수증
X = int(input())
N = int(input())

sum = 0

for i in range(1,N+1):
    a,b = map(int,input().split())
    c = a * b
    sum += c

if sum == X:
    print('Yes')
else:
    print('No')
    
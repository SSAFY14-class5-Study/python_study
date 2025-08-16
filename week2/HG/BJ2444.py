# 별찍기 7

N = int(input())

for i in range(1,N): #삼각형 부분 범위 1,2,3,4까지 
    print(' '* (N- i) +'*'*(2*i-1)) # 2*i-41 홀수만 출력 
# 공백은 4,3.. N-1 개
for j in range(N,0,-1):
    print(' '*(N-j) + '*'*(2*j-1)) #공백 1
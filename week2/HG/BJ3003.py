#킹,퀸,룩,비숍,나이트,폰

a = list(map(int,input().split()))

chess = [1,1,2,2,2,8]

for i in range(0,6): # 0보다 크면 
    # chess[i] = chess[i] - a[i]
    chess[i]-= a[i]
    #왼쪽 변수에서 오른쪽 값을 뺀 후, 그 결과를 다시 왼쪽변수에 대입하라

print(chess)


# 행렬덧셈
# O(N*M)

N, M = map(int, input().split())
final = [[0]*M for i in range(N)]
list_a = []
list_b = []
for i in range(0,N):
    list_a.append(list(map(int,input().split())))

for i in range(N,N+N):
    list_b.append(list(map(int,input().split())))


for r in range(0,N): #행 1개 선택후 순회하는 반복문
    for c in range(0,M): #열 전체 순회
        final[r][c] = (list_a[r][c]+ list_b[r][c])


for i in range(0,N):
    print(*final[i]) # 행 반복문에서 i 로 현재 행 표현
    # * : 괄호벗김 + 자동 공백구분 출력

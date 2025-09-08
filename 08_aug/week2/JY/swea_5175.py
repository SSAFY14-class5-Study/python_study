def inorder(idx, N):
    global tree, cnt

    if idx > N:
        return
    
    inorder(idx*2,N)
    cnt += 1
    tree[idx] = cnt
    inorder(idx*2 + 1, N)

T = int(input())
for tc in range(1,T+1):
    N = int(input())  
    tree = [0] * (N+1)
    cnt = 0
    ans = inorder(1,N)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
   

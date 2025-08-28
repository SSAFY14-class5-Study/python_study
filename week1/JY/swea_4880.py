def beats(a,b):
    return (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2)

def tournament(N,cards):
    cards = [0] + cards

    def winner(i,j):
        if i == j:
            return i
        mid = (i+j) //2
        left = winner(i,mid)
        right = winner(mid+1, j)

        if cards[left] == cards[right]:
            return left if left < right else right
        
        return left if beats(cards[left], cards[right]) else right
    return winner(1,N)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    ans=tournament(N,arr)
    print(f'#{tc} {ans}')

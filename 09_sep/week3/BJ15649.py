# N과 M (1)
def perm():
    if len(S) == M:
        print(' '.join(map(str, S)))
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            S.append(i)
            perm()
            S.pop()
            visited[i] = False

N, M = map(int, input().split())

S = []
visited = [False] * (N + 1)
perm()

# 영화감독 숌
N = int(input())
i = 666
cnt = 0
while True:
    if "666" in str(i):
        cnt += 1
        if cnt == N:
            print(i)
            break
        else:
            i += 1
    else:
        i += 1

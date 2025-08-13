#주사위

a,b,c = map(int,input().split())

# 같은 눈 3개
if a == b == c:
    print(10000 + a * 1000)
# 같은 눈 2개
elif a == b != c:
    print((a*100) + 1000)
elif a == c != b:
    print((a*100) + 1000)
elif b == c != a:
    print((b*100) + 1000)

else:
    d = max(a,b,c)
    print(d*100)
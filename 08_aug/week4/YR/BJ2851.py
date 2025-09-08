# 슈퍼 마리오
after = 0
before = 0

for _ in range(10):
    x = int(input())
    before = after
    after += x
    if after >= 100:
        break

if abs(100 - after) < abs(100 - before):
    print(after)
elif abs(100 - after) > abs(100 - before):
    print(before)
else:
    print(after) 

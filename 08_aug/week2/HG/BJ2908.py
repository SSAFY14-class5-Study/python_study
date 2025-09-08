# 상수

A, B = input().split()

print(A[::-1] if A[::-1] > B[::-1] else B[::-1])  # 삼항연산자
#True 면 출력할 것 if 조건 else False면 출력할 것
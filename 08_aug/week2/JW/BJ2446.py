# 별 찍기 - 9
n = int(input())

for i in range(0, n):
    print(" " * i, "*" * ((n - i) * 2 - 1), sep="")

for i in range(1, n):
    print(" " * (n - 1 - i), "*" * (2 * i + 1), sep="")


# 결과
"""
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
"""

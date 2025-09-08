# 다이얼
word = input()
total_time = 0

for char in word:
    if char in 'ABC':
        total_time += 3
    elif char in 'DEF':
        total_time += 4
    elif char in 'GHI':
        total_time += 5
    elif char in 'JKL':
        total_time += 6
    elif char in 'MNO':
        total_time += 7
    elif char in 'PQRS':
        total_time += 8
    elif char in 'TUV':
        total_time += 9
    elif char in 'WXYZ':
        total_time += 10
        
print(total_time)
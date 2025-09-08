def cycle_length(num):
    start = num
    count = 0

    while True:
        tenth_digits = num // 10
        unuits_digits = num % 10
        digit_sum = tenth_digits + unuits_digits 
        new_num = unuits_digits * 10 + (digit_sum % 10)
        count += 1
        num = new_num

        if start == num:
            return count

N  = int(input())
ans = cycle_length(N)
print(ans)
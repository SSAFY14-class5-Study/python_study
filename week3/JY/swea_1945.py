def factorization_into_primes(num):
    a,b,c,d,e = 0,0,0,0,0

    while num > 1:
        if num % 2 == 0:
            a += 1
            num //= 2
        elif num % 3 == 0:
            b += 1
            num //= 3
        elif num % 5 == 0:
            c += 1
            num //= 5
        elif num % 7 == 0:
            d += 1
            num //= 7
        elif num % 11 == 0:
            e += 1
            num //= 11
    return a,b,c,d,e

T = int(input())
for tc in range(1,T+1):
    num = int(input())
    ans= factorization_into_primes(num)
    print(f'#{tc}', *ans)
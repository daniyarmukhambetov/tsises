def is_perfect(n):
    res = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            res += i
            res += n // i
        i += 1
    return res == n
print(is_perfect(int(input())))
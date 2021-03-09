
def ispr(n):
    ok = True
    i = 2
    while i * i <= n:
        ok &= (n % i == 0)
        i += 1
    return ok
print(ispr(int(input())))
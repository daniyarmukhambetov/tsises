def prod(a):
    res = 1
    for i in a:
        res *= i
    return res
print(prod([1, 2, 3, 4, 5]))

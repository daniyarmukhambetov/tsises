def my_factotial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(my_factotial(int(input())))
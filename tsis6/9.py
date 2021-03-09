def get_even(a):
    aa = filter(lambda a : a % 2 == 0, a)
    print(*aa)
get_even([1, 2, 3, 4, 5])

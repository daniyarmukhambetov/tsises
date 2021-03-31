lst = [1, 2, 3, 4, 5, 6]
def modify_list(a):
    n = len(a)
    for i in range(n):
        if a[i] % 2 == 0:
            a.remove(i)
modify_list(lst)
print(lst)
def find_uniques(a):
    aa = set(a)
    # for i in a:
    #     aa.add(i)
    return list(aa)
print(find_uniques([int(i) for i in input().split()]))
def calc(s):
    n = len(s)
    k = 0
    for ch in s:
        if 'a' <= ch <= 'z':
            k += 1
    return (k, n - k)
l, u = calc(input())
print("Number of lowercase letters", l)
print("Number of uppercase letters", u)

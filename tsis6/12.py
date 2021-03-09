def is_palindrom(s):
    n = len(s) - 1
    ok = True
    for i in range(n // 2 + 1):
        ok &= (s[i] == s[n - i])
    return ok
print(is_palindrom(input()))
# 012345678910 
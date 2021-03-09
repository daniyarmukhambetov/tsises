def rev(s):
    n = len(s)
    res =''
    for i in range(n - 1, -1, -1):
        res += s[i]
    return res 
print(rev('123'))

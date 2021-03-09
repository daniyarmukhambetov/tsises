def f(ss):
    s = ss.split('-')
    print(s)
    s.sort()
    res = s[0]
    for i in range(1, len(s)):
        res += f'-{s[i]}'
    return res
ans = f('green-red-yellow-black-white')
print(ans)
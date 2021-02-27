import re
tt = int(input())
res = ''
while tt != 0:
    tt -= 1
    s, t = input().split()
    s1 = re.match(r'[a-zA-Z]+', s)
    t1 = re.match(r'<[a-z]([a-z-_.0-9]+)@[a-z]+\.[a-z]{1,3}>', t)
    if t1 and s1:
        # print(s1.group(0) + ' ' + t1.group(0))
        res += f'{s} {t}\n'
print(res)

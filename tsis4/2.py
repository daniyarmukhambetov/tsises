# https://www.hackerrank.com/domains/python/py-regex/difficulty:easy/page:1
import re
t = int(input())
while t > 0:
    s = input()
    res = re.search(r'^(\+|-){0,1}[0-9]*(\.)(\d)*$', s)
    if res:
        print(True)
    else : print(False)
    t -= 1
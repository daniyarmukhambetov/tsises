import re
s = input()
res = re.findall(r'(\d+)([a-z]+)', s)
# print(res.group(0))
print(res)

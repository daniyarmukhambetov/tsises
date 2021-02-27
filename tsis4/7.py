import re
s = input()
ans = re.split(r'\.|,+', s)
for ss in ans:
    print(ss)


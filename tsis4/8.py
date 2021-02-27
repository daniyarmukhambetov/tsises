import re
s = input()
res = re.match(r'D{0,1}M*L*C*X*L*X*V*I*')
if res:
    print(True)
else: print(False)
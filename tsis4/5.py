import re
tt = int(input())
while tt != 0:
    tt -= 1
    s = input()
    RE = re.match(r'^[789]([0-9]{9})$', s)
    # print(RE)
    if RE :
        print("YES")
    else :
        print("NO")
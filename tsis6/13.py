import math
def pas(n):
    res = []
    # res1 = []
    for i in range(n + 1):
        res1 = []
        for j in range(i + 1):
            res1.append(math.comb(i, j))
        res.append(res1)
    return res
pas_tri = pas(int(input()))
for aa in pas_tri:
    print(aa)

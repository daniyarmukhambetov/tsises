import math
n = int(input())
ans = 0
pp = pow(n, n - 1)
for i in range(n - 1, 100 * n):
	ans += math.comb(i, n - 1) * (i) / (pow(n, i))
print(ans)
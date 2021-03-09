n, l, r = map(int, input().split())
def is_in_range(n, l, r):
    return l <= n <= r
print(is_in_range(n, l, r))
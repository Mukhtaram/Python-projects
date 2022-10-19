import sys

x, n = map(int, sys.stdin.readline().split())
q = 0

for i in range(n):
    q = x % 10
    if q != 0:
        x -= 1
    else:
        x //= 10
print(x)
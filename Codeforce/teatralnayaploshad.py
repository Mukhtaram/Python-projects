import sys

n, m, a = map(int,sys.stdin.readline().split())
sum = 1
if n > a:
    sum = (n + a - 1)//a
if m > a:
    sum *= (m + a - 1)//a
print(sum)

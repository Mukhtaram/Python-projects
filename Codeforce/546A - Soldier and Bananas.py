import sys

k, m, n = map(int, sys.stdin.readline().split())
sum = 0
b=0
while n != 0:
    sum+= n * k
    n-=1
b = sum-m;
if sum > m:
    print(b)
else:
    print(0)
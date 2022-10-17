import sys

m, k = map(int, sys.stdin.readline().split())
lst = list(map(int, input().split()))
q = 0

for student in lst:
    if student >= lst[k] and student > 0:
        q += 1
print(q)
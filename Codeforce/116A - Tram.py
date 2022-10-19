n = int(input())
sum = 0
q = 0
max = 0
while n > 0:
    a, b =map(int, input().split())
    sum = (b + q) - a
    q = sum
    if sum > max:
        max = sum
    n-=1
print(max)
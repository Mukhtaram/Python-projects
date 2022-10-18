x = int(input())
n = int
if x % 5 == 0 and x > 5:
    n = x // 5
elif x % 5!= 0 and  x > 5:
    n = (x // 5) + 1
else:
    n = 1
print(n)
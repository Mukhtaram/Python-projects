n = int(input())
s = True
q = 0
while n > 0:
    digit = n % 10
    if digit == 7 or digit == 4:
        q+=1
    else:
        q+=0
    n //= 10
if q==4 or q==7:
    print("YES")
else:
    print("NO")

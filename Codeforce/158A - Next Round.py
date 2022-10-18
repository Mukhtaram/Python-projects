a,b = map(int, input().split())
c = list(map(int,input().split()))
q = 0

for i in range(a):
    if c[i] == c[b-1] and c[b-1] == 0:
        q+=0
    elif c[i] >= c[b-1]:
        q+=1
    else:
        q+=0
print(q)

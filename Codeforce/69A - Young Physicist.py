n=int(input())
suma = 0
sumb = 0
sumc = 0
for i in range(n):
    a,b,c=map(int,input().split())
    suma+=a
    sumb+=b
    sumc+=c
if(suma == 0 and sumb == 0 and sumc == 0):
    print("YES")
else:
    print("NO")
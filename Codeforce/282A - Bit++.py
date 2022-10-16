import sys

n = int(input())
ans = 0
for i in range(n):
    x = (input())
    if (x == "X++" or x == "++X"):
        ans +=1;
    if(x == "--X" or x == "X--"):
        ans-=1;
print(ans)

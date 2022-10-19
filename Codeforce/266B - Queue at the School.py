import sys
n, t = map(int, input().split())
s = list(sys.stdin.readline())
q=0
for k in range(t):
    i = 0
    while len(s) - 1 > i:
        if s[i] == "B" and s[i+1] == "G":
            s[i] = "G"
            s[i+1] = "B"
            i+=1
        i+=1
print("".join(s))


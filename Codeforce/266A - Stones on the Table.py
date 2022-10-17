
n = int(input())
s = input()
lst=[]
q = 0
for c in s:
    if c not in lst:
        lst = c
    else:
        q +=1
print(q)
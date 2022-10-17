s = input()
lst = []
for n in s:
    if n.isdigit():
       lst.append(n)
result = "+".join(sorted(lst))
print(result)
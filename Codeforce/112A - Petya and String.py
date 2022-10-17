import sys

s1 = input().lower()
s2 = input().lower()

my_lst = [s1,s2]
if s1 == s2:
    print("0")
else:
    result = min(my_lst)
    if result == s1:
        print("-1")
    elif result == s2:
        print("1")

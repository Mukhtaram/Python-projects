username  = input()
lst = []
my_list = []

for words in username:
    if words not in lst:
        lst.append(words)
if len(lst) % 2 != 0 :
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
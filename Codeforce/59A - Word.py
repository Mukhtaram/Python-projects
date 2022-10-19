s = input()
sumu = 0
suml = 0
sumu = sum(1 for words in s if words.isupper())
suml = sum(1 for words in s if words.islower())
if sumu > suml:
    print(s.upper())
elif sumu < suml:
    print(s.lower())
else:
    print(s.lower())



s = input().lower()
vow = ["aeiouy"]
my_list = []
for letter in s:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
            continue
        else:
            my_list+="."
            my_list.append(letter)
print(*my_list, sep="")

n = int(input())
s = input()
suma = s.count("A")
sumd = s.count("D")
if(suma > sumd):
    print("Anton")
elif(suma < sumd):
    print("Danik")
else:
    print("Friendship")

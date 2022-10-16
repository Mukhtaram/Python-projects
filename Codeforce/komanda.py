n = int(input())
cnt = 0
for _ in range(n):
    z = input()
    if z == '1 1 1' or z ==  '1 1 0' or z == '0 1 1' or z == '1 0 1':
        cnt += 1
print(cnt)
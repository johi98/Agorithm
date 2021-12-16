s = input()

result = 0

for i in range(len(s)):
    if int(s[i]) <= 1 or result == 0:
        result = result + int(s[i])
    else:
        result = result * int(s[i])

print(result)

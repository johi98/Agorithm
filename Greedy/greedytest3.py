s = input()

count1 = 0
count0 = 0

if int(s[0]) == 1:
    count1 += 1
else:
    count0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))

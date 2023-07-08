d = input().split(' ')
r = input().split(' ')
f = 0
for c in range(0, len(d)):
    if int(r[c]) > int(d[c]):
        f += int(r[c]) - int(d[c])

print(f)
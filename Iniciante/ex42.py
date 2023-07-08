a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
v = [a, b, c]
v.sort()
for i in range (0,3):
    print(v[i])
print()
print(a)
print(b)
print(c)
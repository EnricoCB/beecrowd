a, b = input().split(' ')
a = int(a)
b = int(b)
if b == a:
    c = a
elif a > b:
    c = a
else:
    c = b
print(c)
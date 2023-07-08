di = input().split(' ')
di = int(di[1])
hi = input().split(' : ')
si = int(hi[2])
mi = int(hi[1])
hi = int(hi[0])


df = input().split(' ')
df = int(df[1])
hf = input().split(' : ')
sf = int(hf[2])
mf = int(hf[1])
hf = int(hf[0])

if hi > hf:
    d = df - di - 1
    h = (hf - hi) + 24
else:
    d = df - di
    h = hf - hi
if mi > mf:
    m = mf - mi + 60
else:
    m = mf - mi

if si > sf:
    m = 59 - (mi - mf)
    s = sf - si + 60
else:
    s = sf - si

if mi > mf:
    h = (hf - hi) 
elif mi == mf and si > sf:
     h = (hf - hi) + 23
    
if hi == hf:
    if mi > mf:
        d -= 1
    elif si > sf:
        d -= 1

print(f'{d} dia(s)')
print(f'{h} hora(s)')
print(f'{m} minuto(s)')
print(f'{s} segundo(s)')

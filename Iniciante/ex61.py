d = str(input()).split()
d = d[1]
di = int(d)
t = str(input()).split()
hi = t[0]
mi = t[2]
si = t[4]
hi = int(hi)
mi = int(mi)
si = int(si)
d = str(input()).split()
d = d[1]
df = int(d)
t = str(input()).split()
hf = t[0]
mf = t[2]
sf = t[4]
hf = int(hf)
mf = int(mf)
sf = int(sf)

if si < sf:
    s = sf - si
elif si > sf:
    s = (60 - si) + sf
else:
    s = 0

if hi == hf:
    h = 0
    if mi < mf:
        m = mf - mi
        d = (df - di) - 1
    if mi > mf:
        m = (60 - mi) + mf
        d = (df - di) - 1
    if mi == mf:
        m = 0
        d = df - di

print('{} dia (s)'.format(d))
print('{} hora (s)'.format(h))
print('{} minutos (s)'.format(m))
print('{} segundo (s)'.format(s))

'''if hi > hf:
    h = (24 - hi) + hf
else:
    h = hf - hi'''
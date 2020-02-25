# Reverse Word Order

s = 'This is an example'

t = s.split()
u = []
for word in t:
    u.insert(0, word)

print(s)
print(t)
print(' '.join(u))

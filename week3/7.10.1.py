a = []
for i in range(210, 231):
    a.append(i)

res = [sub for sub in a if len(set(str(sub))) == len(str(sub))]

print(str(res))
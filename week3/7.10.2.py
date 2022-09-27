string = input("enter the str: ")
s = string.split()[::-1]
w = []
for i in s:
    w.append(i)
print(" ".join(w))
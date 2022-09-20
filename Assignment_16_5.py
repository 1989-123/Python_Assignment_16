""" Write a python program to check if all items in 
the tuple are the same. """

t1 = (1, 2)
l1 = []
for i in t1:
    if i not in l1:
        l1.append(i)
i, c = 0, 0
while i < len(l1):
    c += 1
    i += 1
if c == 1:
    print()
    print("All elements in tuple are same")
    print()
else:
    print()
    print("All elements are tuple are not same")
    print()

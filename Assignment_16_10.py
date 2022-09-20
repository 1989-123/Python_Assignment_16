""" 
Write a python program to change the first item (22) of a list 
within the following tuple to 222.tuple1 = (11, [22, 33], 44, 55)
"""

tuple1 = (11, [22, 33], 44, 55)
l1 = list(tuple1)
i = 0
while i < len(l1):
    if l1[i] == [22,33]:
        l1[i] = [222, 33]
    i += 1
tuple1 = tuple(l1)
print()
print(tuple1)
print()

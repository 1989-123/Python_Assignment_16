""" 
Write a python program to copy elements 4 and 5 from the following 
tuple into a new tuple. tuple1=(1,2,3,4,5,6)
"""
tuple1 = (1, 2, 3, 4, 5, 6)
l1 = []
tuple2 = ()
for i in tuple1:
    if i == 4 or i == 5:
        l1.append(i)
tuple2 = tuple(l1)

print()
print(tuple2)
print()

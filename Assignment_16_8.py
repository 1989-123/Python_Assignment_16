"""
Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29)) 
"""

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29)) 
tuple2 = []
for i, j in tuple1:
    tuple2.insert(i, j)
print(tuple2)

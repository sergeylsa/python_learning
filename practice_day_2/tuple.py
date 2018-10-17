#tuple
t = (1, 2, 3)
print(t)
print(t[0])

t = ('str', 1, 0.3, True, None)
print(t)
print(len(t))

t2 = (1,2,3)

t3 = t2 + t
print(t3)

print(t3 * 3)

#collection with 1 element
t = (2)#no
print(t)
t = (2, )
print(t)

print((2) == (2, ))

#tuple not modified
t = (1,2,3)
#t[0] = 15

#delete tupel

##create empty tuple
t = tuple()

print(type((1)), type(t))

# tuple operations:
tuple1 = (1, )
tuple2 = (1, )
not_a_tuple = (1)
empty_tuple = tuple()
# add:
tuple1 = tuple1 + tuple2
print(tuple1)

tuple1 = (2, ) + tuple1 + (not_a_tuple, )
print(tuple1)

# indexing:
print(1 in tuple1, 2 in tuple1)

print(len(tuple1), len(tuple2), len(empty_tuple))
print(tuple2[0], tuple1[0:2], tuple1[:-1])

# tuple1[0] = "you can assign to tuple's items! they are read-only."
print(tuple1)

# removing:
# There's no direct way to delete an element from the tuple:
tuple1 = (1, 2, 'string', 'one more', )
print(tuple1)

new_tuple = tuple()
 
for item in tuple1:  # tuple is iterable
    # we will remove all the 'strings' from tuple1
    # if not isinstance(item, (str, unicode)):  # or `basestring`
    if not isinstance(item, str):
        new_tuple += (item, )
print(new_tuple)
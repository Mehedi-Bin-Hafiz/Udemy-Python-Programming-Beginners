#in python variable act as pointer to the memory location
v1=50
v2=v1
print(id(v1))
print(id(v2))
# in python v2 point the same value that is pointed by v1
# so their id are same

v3=50
print(id(v3))

# above three variable point same memory location because their values are same

v1=10
print("New V1 ",id(v1))
print("previous V2 ",id(v2))
# now v1 locate another memory address that contains 10 but v2 still point the memory location of 50
# So the content of memory location are not changed, the pointer is pointed new memory location after the new assignment

"""that means the objects of immutable(অপরিবর্তনীয়) data type can not be changed after they are created"""

# int, float, bool, str, tuple, unicode are immutable , list set and dict are mutable because their value is changeable after creation.


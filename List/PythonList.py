#in python list contains the address of elements
# list is mutable data type
lis1=['mehedi','hasan']
lis2=['mahim','mehedi']
#contains same id though they from different list
print('id of mehedi in list1',id(lis1[0]))
print('id of mehedi  list2',id(lis2[1]))
#id are different as elements are different
print(id(lis1[1]))
print(id(lis2[0]))


# VVI code for get value for a ID
# import ctypes
# a = "hello world"
# b=id(a)
# print (ctypes.cast(b, ctypes.py_object).value)

print("id of lis1 before append",id(lis1))
lis1.append(1)
print(lis1)
print("id of lis1 before append",id(lis1))


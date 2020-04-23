
tup=(1,2,3,4,5,[1,2,'find me',3,4])
#return true if all elements of the tuple or if the tuple is empty
print(all(tup))
tup=(0,1)
print(all(tup)) #it returns false because 0 is considered as false in boolean
tup=(1,2,3,4,5,3)
print(max(tup)) # it works with int, float datatype
print(min(tup)) # it works with int, float datatype
#sum function returns sum of all elements in tuple
print(sum(tup))

#tuple() constructor if we need to convert list to tuple or string to tuple then we use tuple constructor
py="MehediBinHafiz"
print(tuple(py))
lis=[1,2,3,4,5,3]
print(tuple(lis))
#index method returns index of an element
print(tup.index(4))
# count method returns number of times an elements appears in a tuple
print(tup.count(3))





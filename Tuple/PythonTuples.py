#Tuples is a ordered collection of objects, similar to list but immutable data type
# Tuples is created py ()
# since tuple is a immutable data type so it is faster than list

lis=["1"]
tup=("1",) # for single element if we don't add , then not tuple
print(id(lis),id(tup))
print(type(tup))

tup=(1,2,3,4,5,[1,2,'find me',3,4])

print(tup[5][2])

#sliceing in tuple

print(tup[ : : -1]) #(::stride)

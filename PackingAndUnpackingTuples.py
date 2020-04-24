#A python tuple can be created without parentheses. This called tuple packing.
# Python tuples unpacking happens when we assign values from a tuple to a sequence of variables in python
tup=1,2,3 #packing
print(tup)

#it is as like swapping
x=10
y=2
x,y=y,x # y,x converted as tuple first (2,10) it is known as packing
#then 2 assign to the x and 10 assign to the y it is known as unpacking

# so we can unpacking the value of tup
a,b,c=tup #it is the process of unpacking

print(a,b,c)



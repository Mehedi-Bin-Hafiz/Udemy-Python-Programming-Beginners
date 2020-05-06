

"""Polymorphism  poly=many morph=form (একটা জিনিসের অনেক রূপ )"""

"""Part of polymorphism 1. Duck typing 2. Operator Overloading 3. Method Overloading . 4.Method Overriding"""


# in python every operation is a part of its own function
# len('hello') = hello.__len__()

x,y,z=3,4,8
print(x.__add__(y).__add__(z)) # I overwrite __add__ function instead of + object

lis=[1,2,3,4,5]
lis2=[6,7,8,9,0]
new=lis.__add__(lis2)
print(new)
mul=lis.__mul__(2) #it squire lis
print(mul)


# A simple Python function to demonstrate
# Polymorphism

def add(x, y, z=0): # when we define z=0 it act as polymorphic function
    return x + y + z


# Driver code
print(add(2, 3))
print(add(2, 3, 4))

# Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class.





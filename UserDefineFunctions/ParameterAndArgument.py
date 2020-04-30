# a parameter or parameter variable is a variable in the function header which receive an argument when the function is called.
# An argument is nothing but a piece of data passed to the function, when it is called

def add(a,b): # here a and b are parameters
    return a+b
m=add(3,4) # here 3 and 4 are argument
print(m)
#pyhton matches parameter by position.

#keyword argument, By keyword argument we can send argument in any order when we call the function

def subt(first,second):
    return first-second
r=subt(second=10,first=15)
print(r)
#default value
def identity(firstname='Mehedi',lastname='hasan',age=23):
    return firstname+" "+lastname+" and age is "+str(age)
print(identity())

""" We can pass positional and keyword argument at a time. """

print(identity('Mahim',age=10)) # keyword argument followed by  Positional argument other wise error will be produced.




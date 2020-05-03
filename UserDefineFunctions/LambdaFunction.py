# lambda has no name. It is a anonymous function

# syntax lambda parameter : function body (also known as expression)

a=(lambda x,y : x+y) (2,3) #passing value to lambda function

b = lambda x,y,z : x*y*z

print(b(1,2,3))



# The map function map(function, sequence) The map() function in python takes in function in python takes in a function list as argument. And function is applied on each element of sequence


def addition(a):
    return a
a=list(map(addition(a),[1,2,3,4,5,6]))
print(a)


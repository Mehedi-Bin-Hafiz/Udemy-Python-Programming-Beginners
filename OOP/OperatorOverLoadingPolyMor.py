

a=5
b=6
# The type of a is 'int' . because a is a instance of int class as 5 is an integer number.
#every class have different function. So 5 has different function. we can see the function by this code

#print(dir(type(a)))

#by default int class has many built in function that we can see console
print(a+b) # behind the scene + call __add__() method of int class
# so we can write this code

print(int.__add__(a,b))
#or
print(a.__add__(b))

"""concept of operator overloading"""


class Addition:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other): #it is operator overloading  #self refer s1 and other refer s2
        m1=self.m1+other.m2
        m2=self.m2+other.m2 # here other is 4 or 3 an self is 2 or 5
        s3=Addition(m1,m2)
        return s3

s1=Addition(8,4)
s2=Addition(5,3)

s3=s1+s2
print(s3.m2)
# it produce class Student. now we can see which method Student contains

#print(dir(s1)) # we can see there is no __add__(),sub etc method

# so we can not add this s1,s2 object
# lets try
#print(s1+s2) #TypeError: unsupported operand type(s) for +: 'Student' and 'Student'



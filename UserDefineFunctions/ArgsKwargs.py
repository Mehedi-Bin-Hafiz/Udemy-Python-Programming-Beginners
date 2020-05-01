# this is a technique to pass variable number off arguments
# *args this is now keyword arguments that is used to pass multiple argument values to a function
""" Note that in such case argument passed as tuple"""

def addition(*args):
    print(args)
    print(type(args))
    print(sum(args))
addition(1,2,3,4,5)

# if we want to pass keyword argument then we can use **kwargs
# argument pass as dictionary
def sample(**kwargs):
    print(type(kwargs))
    print(kwargs)
sample(a='mehedi',b='hasan')
sample(first='Mahim',last='Hasan')

# we can also send *args as arguments
def add(a,b):
    print(a,' ',b)

v=(1,3)
add(*v) #this asterisk unpack tuple to variable

m=(1,4)

# we can send dictionary by this process
# parameter sequence function(1,*args,keyword,**kwargs) that means 1 formal argument non key word arguments, keyword arguments
def check(a,b,c):
    print(dic.items())
    print(dic.values())
    print(a,b,c)
dic={1:'mehedi',2:'bin',3:'hafiz'}
check(*dic)


#nam korton -->  Name Mangling is to avoid the risk of conflict when designing classes for inheritance.!

# Python interpreter applies name mangling to protect the variable from being overridden in subclasses.
# The way of name mangling is add double underscore in a variable or function.
# when we add __ then python automatically mangle it _class__function or variable name.
# By name mangling we can create private variable or function

class Test1:
    def __init__(self):
        self.f="mahim"
        self.__l="hasan"
        self.full=self.f+self.__l
    def fullname(self):
        return self.f+self.__l
    def __mehedi(self):
        print('nearly impossible to call directly')

    def get_attr(self): #it access the value
        return self.f+" "+self.__l
    def set_attar(self,value):
        self.__l=value

class Test2(Test1): # it can change the value
    def __init__(self):
        super().__init__()
        pass

T2=Test2()
print(T2.f)
#print(T2.__l) #we can not access it

T1=Test1()
#  print(T1.__l) # Even we can not access it by its own class instance


print(T1.full)
print(T2.fullname())
#print(T1.__mehedi) it produce error

# but we can access private variable and function if we know the class name and the variable of function name. but this is not legal.

print(T2._Test1__l)
T1._Test1__mehedi()
# but this not  not good idea


# we can change it by getter and setter. and always try to change it getter and setter

print(T1.set_attar("bin hafiz"))
print(T1.get_attr()) # it is convention way

print(dir(Test1))

"""this is all about this course"""
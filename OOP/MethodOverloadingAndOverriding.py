# Method OverLoading

# class Student:
#     def average(self,mid,final):
#         self.mid=mid
#         self.final=final
#
#     def average(self,quiz,atten,pre):
#         self.quiz=quiz
#         self.atten=atten
#         self.pre=pre

"""if we have a class and that class has to method of same name but different parameters then it called method overloading. but in python we can not create two method with the same name in a class. So we need to do method overloading technically. """


#example

class Student:
    """"Important notice we need to define 0 in function parameter and inside of function we need to use None otherwise it will not work"""
    def __init__(self,mid=None,final=None,):
        self.mid=mid
        self.final=final
    def MethodOverLoading(self,quiz=0,atten=0,pre=0):

        res=0

        if quiz!=None and pre!=None:
            res=quiz + pre
            print("sum of quiz and presentation: ",res)
        elif quiz!=None and atten!=None and pre!=None:
            res = quiz + atten+pre
            print("sum of quiz,presentation and attendance: ", res)
        else:
            print("you pass no argument")




obj=Student(1,3)

#print(Student.__doc__)
obj.MethodOverLoading(2,pre=5)

##########Now Method Overriding#############

"""Without inheritance method overriding is impossible"""

class A:
    def phone(self):
        print("nokia 1110")
class B(A):
    def show(self):
        pass
    def phone(self): # now B call only its own phone. Not his father phone. it is called method overriding
        print("Huawai")

o=B()
B.phone(o)
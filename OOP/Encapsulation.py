# Encapsulation ensure that the safe storage of data in a class to prevent unauthorized access

#public---> accessed by any class
#protected---> accessed by child class
#privet---->accessed by class itself

# Encapsulation in python lacks strict access control
#পাইথনে এনক্যাপসুলেশনে কঠোর অ্যাক্সেস নিয়ন্ত্রণের অভাব রয়েছে
# Because most of object are free
class Department:
    def __init__(self):
        self.id='12345'
class Employee(Department) :
    def __init__(self):
        super().__init__()


obj=Employee()
print(obj.id)
# now i want to change the value of id by employee instance: if we maintain encapsulation it is impossible
obj.id='mehedi'
print(obj.id)
# we can see value is changed
dep=Department()
print(dep.id)

"""Python doesnt have private keyword. In order to maintian private keyword python use .__variableName. Single _under score also represent private but it dose not mean we can not change the value. In such case value is changeable"""


class Test1:
    def __init__(self):
        self.f="mahim"
        self.__l="hasan"
        self.full=self.f+self.__l
    def fullname(self):
        return self.f+self.__l
class Test2(Test1):
    def __init(self):
        super().__init__()
        pass

T2=Test2()
print(T2.f)
#print(T2.__l) #we can not access it

T1=Test1()
#  print(T1.__l) # Even we can not access it by its own class instance


# Now try to access modifying __l
print(T1.full)
print(T2.fullname())


"""This is all about this topic"""
# Encapsulation ensure that the safe storage of data in a class to prevent unauthorized access

#public---> accessed by any class
#pretected---> accessed by child class
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
dep=Department()
print(dep.id)
# we can see value is changed



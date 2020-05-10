# it is a process of creating one class from an existing  class

# Overriding is the ability of a class to change the implementation of a method provided by one of its ancestors

class HafizurRahman:
    special = "only mehedi can access it"
    def __init__(self,age,height,occupation):
        self.age=age
        self.height=height
        self.occupation=occupation
    def information(self):
        print('Details of Hafizur Rahman: ')
        print('Age:',self.age)
        print('Height:',self.height)
        print('Occupation:',self.occupation,"\n\n")
    def phone(self):
        print('Only Mahim can get his father phone')

class ElderChild(HafizurRahman):
    def __init__(self,name,age,height,occupation):
        self.name=name
        super().__init__(age,height,occupation) # access parent class attribute. All attribute must be included


    def information(self):
        m=super().special #Process of accessing attribute of parent class
        print(m)
        print('Name: ', self.name)
        print('He is a elder son of Hafizur Rahman')
        print('Age:', self.age)
        print('Height:', self.height)
        print('Occupation:', self.occupation,'\n\n')
    def BSCINCSE(self):
        print("Mehedi reads in CSE")


class YoungerChild(HafizurRahman):
    def __init__(self,name,age,height,occupation):
        self.name=name
        super().__init__(age, height, occupation)

    def information(self):  #it is call override

        print('Name: ',self.name)
        print('He is a younger son of Hafizur Rahman')
        print('Age:', self.age)
        print('Height:', self.height)
        print('Occupation:', self.occupation)
        #super().information() # if we want to call override function we can also by this way
    def ClassSeven(self):
        print("Mahim reads in class Seven")

parent=HafizurRahman('55',5.7,'Businessman')

parent.information()

"""The instance of parent class can not access the child class elements But child class instance can access parent class elements"""

Mehedi=ElderChild('Md.Mehedi Hasan',24,5.7,'Student')
Mehedi.information()


Mahim=YoungerChild('Md.Mahim Hasan',14,5.5,'Student')
YoungerChild.information(Mahim)
Mahim.phone()




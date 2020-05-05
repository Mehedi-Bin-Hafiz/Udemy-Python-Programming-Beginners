class CallMe():
   """ self a parameter that invoke instance automatically """ # doc must be set in first
   clsattri=1
   clsattri2=2
   def __init__(self,insattri,insattri2):
       self.insattri=insattri
       self.insattri2=insattri2
   def FullName(self):
       return self.insattri +' '+self.insattri2
   def Addition(self):
       return self.insattri+self.insattri2
   def Subyclsins(self):
       return CallMe.clsattri2-CallMe.clsattri
   def change(self):
       CallMe.clsattri=10
       print('New clsatri ',CallMe.clsattri)
   def my(self,brother):
       print(brother) # local variable for this funcion




instance1=CallMe('mehedi','hasan')
print(instance1.FullName()) #way 1
print(CallMe.FullName(instance1)) #way 2


# Accessing instance attribute
m=instance1.insattri
print(m)
# Accessing class attri
e=CallMe.clsattri
print('class attri',e)


instance2=CallMe(2,2)
result=instance2.Addition()
print(result)

instance3=CallMe(3,4)
re=instance3.Subyclsins()
print(re)

instance3.change()

instance3.my('mahim hasan')

print(CallMe.__doc__)
print(instance3.__dict__)









#Alising=the misidentification of a signal frequency, introducing distortion or error.
#aliasing happens when one varibale's value is assigned to another variable for mutable datatype
lis1 =[1,2,3]
lis2 =lis1

print(lis1 is lis2)
# output is true because they point same memory location

# What about list2 if we any change of lis1 example:
lis1.append('4')
print("new list1",lis1)
print("list2 ",lis2) # as list2 point same memory location that is pointed by list1 so for mutability if we do any change of lis1 then list2 affected this is called aliasing list
print(lis1 is lis2)

#so we can say if data is immutable then aliasing doesnt matter but data is mutable then aliasing is happened

""" we prevent this situation by copy list """

lis3=lis1.copy()
print(lis3 is lis1)

# now there is no effect of aliasing

lis1.append(2)
print(lis1)
print(lis3)

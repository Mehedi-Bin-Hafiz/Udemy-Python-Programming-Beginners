#append method
lis=[1,2,3,4,5,6]
lis.append('mehedi')
print(lis)

#extend method add one list to another list. It maintain iterable technique
lis2=['hasan','7','8','9']
lis.extend(lis2)
print(lis)
# By concatenate list we can add two or more list and generate new list
lis3=lis+lis2
print(lis3)

#list insert
lis.insert(3,"new") #(first one is index number, second one is value)
print(lis)
#pop(argu) method here param is a index number that of element that we want to remove. pop remove element permanently
lis.pop(7)
print("remove 7 position",lis)
lis.reverse() #it reverse the list permanently
print(lis)

#copy() method can be use to copy another list to new list
cop=lis.copy()
print("copy list", cop)

#anoter way
cop=lis[:]
print("another way", cop)

# is they point same memory location? checking by identity method
print(cop is lis)
# false so they point another method

# short and shorted it work only same data type
sor=["mehedi","always"]
sor.sort() #sort() method sort list permanently
print(sor)

sor=[1,2,6,4,3]
sord=sorted(sor) # sorted function return new list that's why we need to store it to another variable
print(sord)




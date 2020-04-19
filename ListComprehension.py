# comprehension allow us to create sequences from other sequence

#syntax lis=[compression(it is output result by item of list 1 which must be same name of item) for item in list]

lis1=[1,2,3,4,5,6,7]
lis2=[ i for i in lis1]
print(lis2)

#create squire number

lis3=[i*i for i in lis2]
print(lis3)

# list of even number on a lis1
evenlis=[i for i in lis2 if i%2==0]
print(evenlis)


#list constructor "here the parameter must be  iterable
number="83472598340589534832342589"
print(list(number))

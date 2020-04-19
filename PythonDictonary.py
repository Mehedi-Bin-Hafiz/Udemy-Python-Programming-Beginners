# dictionary is a key value pair data satructure
# mutable , unsupported duplicate key
#dictionary key is immutable
# it has function dict(argument as a [list contains key value pair])
dit={'a':'mehedi','b':'hasan','c':'bin','d':'hafiz'}
print(type(dit))
print(dit)

for value in dit.values():
    print(value)

# create dictionary by dict function
dit2=dict([('a',1),('b',1),('c',1)])
print(dit2)

#print single element

print(dit['a'])

# list in a dictionary
dit3={1:"mehedi",2:'hasan',3:["mahim",'find me','hasan']}
print(dit3)

print(dit3[3][1])

#nested dictionalry
dit4={1:"mehedi",2:'hasan',3:["mahim",'find me','hasan'],'sub':{'a':'mehedi','b':'hasan','c':'find me'}}
print(dit4)

print(dit4['sub']['c'])

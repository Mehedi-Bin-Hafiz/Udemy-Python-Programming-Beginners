dit={'a':'mehedi','b':'hasan','e':'bin','d':'hafiz'}
print('a' in dit)
print('a' not in dit)

#comparision operator
dit2={'a':'mehedi','b':'hasan','e':'bin','d':'hafiz'}
print(dit==dit2) # are they contains same key value
print(dit!=dit2)

# it return all key in a dictionary. same way we can get value using dit.value()
for key in dit.keys():
    print(key)

#print key value pair
for item in dit.items():
    print(item)

dit={'a':'mehedi','b':'hasan','e':'bin','d':'hafiz'}
#sorted based on value

ditf=sorted(dit.values()) #it returns sorted value
print(ditf)

#get method to find the value
print(dit.get('b'))
# if there is no key then it does not rise error instead of it returns None
print(dit.get('l','nai')) # in this case it returns nai

#items() method returns key-value pair
print(dit.items())
#keys() returns the list of keys
print(dit.keys())
#values() returns the list of value
m=dit.values()
print(m)

#pop method remove the key and returns the value of that key
print(dit.pop('a'))
print(dit)

#update(argument as a dict) that marge two dict

dit2={'a':'mehedi','b':'hasan','e':'bin','d':'hafiz'}
print(id(dit),id(dit2))

d={'q':'mehedi','w':'hasan','e':'haha','t':'hafiz'} #if key is match then update method replace the older value and insert update value
dit2.update(d)
print(dit2)

#del method to remove aye key value from a dict
del dit['b']
print(dit)
print(len(dit))


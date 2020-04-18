# if we don't return any value inside bool method it returns false
print(bool())
print(bool('mehedi'))
print(bool(2.0))
print(bool(0))

#we can store boolean value in to a variable
x=bool(4<1)
print(x)

# not as a complement
print(not(10==10)) #returns false

# in, not in are membership operator
#is, is not are identity operator

a=10
b=10
#
# print(id(a))
# print(id(b))

print(a is b) #return true because they point same address
print(a is not b) #return false
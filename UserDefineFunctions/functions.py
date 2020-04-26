#syntax def func_name(para1,para2):
     #statement
#call
#finc_name(arg1,arg2)
#we need to define function first then call it otherwise name error produce

def greet(n):
    for i in range(1,n+1):
        print(i)

greet(10)

# if function have return() then it called value returning function
# if function does not have return() function then it called void function

print("add function")
def add(a,b):
    print(a+b)

d=add(2,3)
print(type(d))

def min(a,b):
    if a > b:
        return b
    else:
        return a
res=min(9.0001,9.001)
print(res)
print(type(res))

def test():
    return  #return none
x=test()
print(type(x))

#call inside call
def mul(a,b):
  return a*b
res=mul(3,mul(2,3))
print(res)





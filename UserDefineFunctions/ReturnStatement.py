# if function have return() then it called value returning function
# if function does not have return() function then it called void function
def sum(a,b):
    return
m=sum(2,4)
print(m)

#we can use multiple return statement but when one statement is counted then function stop its work

def signal(flag):
    if (flag=='green'):
        return('process')
    else:
        return('unprocess')
res=signal('mehedi')
print(res)

#return multiple value from a funcion

def calculator(a,b):
    s=a+b
    d=a-b
    m=a*b
    try:
        di=a/b
    except:
        di=b/a
    return (s,d,m,di)
res=calculator(10,5)
a,s,m,d=res
print("addition is ",a)
print("subtraction is ",s)
print("multiplication is ",m)
print("division is ",d)


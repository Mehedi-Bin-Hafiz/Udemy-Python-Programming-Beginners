# namespace is a mapping process to locate value and variable name it is as like as dictionary

# every function has its own namespace
c=5
def mehedi():
    #print(c)
    c=3 #Local variable
    print(c)
mehedi()
print(c)
# when python search a variable it follows specific rule:
# Local-Enclosed-global-builtin  (enclosed means nested)

print('new ')
v=1
def check():
   v=2
   print(v)
   def inside():
       v=3
       print(v)
   inside()
print(v)#global v is printed

check()

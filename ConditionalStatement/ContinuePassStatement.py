# continue statement help us to escape normal flow
b=[1,2,4,2,-2,-3,5,-6]

for i in b:
    if(i<0):
        continue # it take for loop and order to perform next iteration
    else:
        print(i*i)

for i in b:
    if(i<0):
        break # it terminates for loop  permanently when it founds less than 0
    else:
        print(i*i)

#pass statement can be use when the program require no action. Some time it is a necessary for us

for i in b:
    if(i<0):
        pass # it pass when i < 0
    else:
        print(i*i)

#another example
color='green'
if(color=='red'): #condition is false so it executes else statement
    print('go')
elif(color=='green'):
    print('impossible') #after execute elif and if it is true then after execute if will be terminated
else:
   pass #when no need to use else then we can use pass for maintaining actual program flow

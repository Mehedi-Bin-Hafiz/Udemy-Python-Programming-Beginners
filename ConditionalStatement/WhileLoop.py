#while loop executed until condition is true.
# so we can create infinite loop by while loop
# a=1
# while(a>0):
#     print(a*2)
#     a=a+1
# while(True):
#     print('mehedi')

v=10
while(v>0):
    if v==5:
        break # now else statement does not executed. Because while loop does not end normally
    print(v)
    v=v-1
else:
    print("condition is false")
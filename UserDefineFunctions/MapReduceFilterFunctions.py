#reduce function. The reduce function work with each pair element of single list
from functools import reduce
maxvalue=reduce(lambda x,y: x if x>y else y,[4,3,5,3,4,5,23,0])
print(maxvalue)

# filter(function, sequence) it also take function and list as a parameter. it apply this function each of the elements of the list.and if the condition is true then the element included as output

fil=filter(lambda x: x%2==0, [1,2,3,4,4,6,7,8])
print(list(fil))

# if the X%2 is true for any list element then this elements included as output.

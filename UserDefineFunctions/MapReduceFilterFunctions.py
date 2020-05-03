#reduce function. The reduce function work with each pair element of single list
from functools import reduce
maxvalue=reduce(lambda x,y: x if x>y else y,[4,3,5,3,4,5,23,0])
print(maxvalue)
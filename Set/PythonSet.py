# A set is a unordered collection of data with no duplicate elements
# sets are iterable and mutable
# A set is created by placing all the elements inside curly braces . separated by comma or by using the built in function set()
# caution : set itself is a mutable but it can not contain mutable data set ten it produce error

# be aware a=  {} represent dictionary
s ={ 'python', 'mehedi', 'hasan',1,2,1,1,2,3,4,5,5}

print(s)
#python automatically remove  duplicate value from the set


x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x)


# but set contains any tuples because tuple is immutable
s ={ 'python', 'mehedi', 'hasan',1,2,1,1,2,3,4,(5,5)}
print(s)
# s ={ 'python', 'mehedi', 'hasan',[1,2,1,1,2],3,4,(5,5)}
# print(s) produce type error

#add() method can add only immutable data. as set is a unordered data type so element can be added any index

#add(), clear(), update(), discord(), remove() mehtods
s.add(12)
print(s)

s.update([88,99,1,2])
print(s) # if we want to add two set we can do it by update method

#dicard() method

s.discard(88) # it produce no error if there is no element
print(s)
# s.remove(88) # it produce key error if there is no element
# we can use pop() method to remove 1st element from set








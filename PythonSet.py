# A set is a unordered collection of data with no duplicate elements
# sets are iterable and mutable
# A set is created by placing all the elements inside curly braces . separated by comma or by using the built in function set()
# caution : set itself is a mutable but it can not contain mutable data set ten it produce error

# be aware a=  {} represent dictionary
set ={ 'python', 'mehedi', 'hasan',1,2,1,1,2,3,4,5,5}

print(set) #python automatically remove  duplicate value from the set




# set ={ 'python', 'mehedi', 'hasan',1,2,1,1,2,3,4,5,5,[1,2,3,4,5]}
# print(set)

# set ={ 'python', 'mehedi', 'hasan',1,2,1,1,2,3,4,5,5,{1,2,3,4,5}}
# print(set)


### it produce type error

# but set contains any tuples because tuple is immutable
set ={ 'python', 'mehedi', 'hasan',1,2,1,1,2,3,4,(5,5)}
print(set)


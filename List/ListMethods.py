lis=[1,2,2,4,5,6,7]

lis.append(8) # it add element last index of the list.it can add another list, tuple or dict. but it can not add more than 1 single element.
print(lis)
# to add more than one single element we can use extend method.
# extend(param) here param is iterables. we know in python iterables are list,tuple and set and strings.
# the extend() method. Add elements of a list to another list.
lis2=[9,10]
lis.extend(lis2)
print(lis)

# insert(index,element). by insert method we can add element in specific index
lis.insert(2,'new')
print(lis)
# remove(param) it can remove item from list. it search element from list and remove it. note if there is any duplicate then first one will be deleted.
lis.remove(2)
print(lis)
# note if there is no matching element then it produce error.
#lis.remove('mehedi')


# index() by this method we can see the index of an element. and of course it return first index of duplicate element

print(lis.index(2))

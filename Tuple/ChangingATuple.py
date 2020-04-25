#tuples are immutable but it can contain mutable objects when tuples contains mutable objects then this objects is changeable

tup=(1,2,3,4,5,['a','b','c'])
print(id(tup))
print('List Id',id(tup[5]))

#now we will try to change list element
tup[5][1]="i am new"
print(tup)
print("list id after changing",id(tup[5]))
print("Tuple id same",id(tup))

#list id same

#contatination of tuple

tup2=tup+tup
print(tup2)
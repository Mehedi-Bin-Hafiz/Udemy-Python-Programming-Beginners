#union() produce common uncommon value one time not duplicate
a={1,2,3,4,5}
b={2,3,6,8,0,7,10}
u=a.union(b)
print(u)
# intersection produces only common value from two set
i=a.intersection(b)
print(i)
#difference method print set the value of set a which are not in set b
print(a.difference(b))

#isdisjoint() return true if sets have a null intersection that means there is no common value
print(a.isdisjoint(b)) # produce false because there are common value is existed
#if any set contains other's set elements then it's called subset
print(a.issubset({1,2,3,4,5}))
#if any set contains any of  other's set elements then it's called superset
print(a.issuperset({1,2,3}))

#iteration of set
for i in b:
    print(i)
#sorted() function
print(sorted(b)) #it produce sorted list





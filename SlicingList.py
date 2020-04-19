lis=[1,2,3,4,6]
#insert value inside list
lis.insert(4,5) #first one is index number and second one id value
print(lis)

print(lis[2:4]) # here 1st index is starting index and last

# stride = a step or stage in progress toward an aim.
# list has 3 parameter [start index : end index : stride ]
# by default stride set as 1
print(lis[ : : 2]) # first to last index and stride 2

# reverse list by stride parameter

print(lis[ : : -1])



# generators in python are just another way of creating iterable objects.
# a generator uses a yield statement instead of return statement to generate values


# generator will give you iterator

def topten():

    yield 1
    yield 2
    yield 3

    # normally function have return value. when we return value it return only this value. But we want to iteration. so generator used yield for iteration instead of iteration. yield is a special function which will make your function to iterator.




val=topten()

print(val.__next__())
print(val.__next__())

for i in val:
    print(i)



print("print top ten")
def topte():
    n=1

    while n<=10:
        yield n
        n+=1

v=topte()
for i in v:
    print(i)



print("use generator instead of list comprehension")

g=(x for x in range(1,11))
print(g) # is a generator object


print("access one by one")
print(next(g))
print(next(g))

print('using for loop')
for i in g:
    print(i)
# what is iterable?

#an object that can be looped over using a for loop is called iterable
# an iterable has the __iter__ method defined.
# List, Strings, Tuples,Sets, dictionaries, files and generator are examples of Iterables.


x=[x**2 for x in range(5,25,5)]
print(x)

dit={1:'a',2:'b',3:'c'}
for i in dit.values():
    print(i)

## run while loop over list
n=0
while n < len(x):
    print(x[n])
    n=n+1

print('reverse')
n=len(x)-1
while n > -1:
    print(x[n])
    n=n-1



# what is iterator?
# ans: an iterator is an object which represents a stream of data
# An iterator allows you to iterate over a container
# The iterator in python is implemented via two method: __iter__ and  __ next__
# The __ iter__ method is required for your container to provide iteration support. it will return the iterator object itself.
# The __next__ method weill return the next item in the container
print("iterator ")
it=iter(x)
print(it.__next__())
print(next(it))

## custom iterator !!!

class topten:
    def __init__(self):
        self.n=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<=10:
            val=self.n
            self.n=self.n+1
            return val
        else:
            raise StopIteration

val=topten()
for i in val:
    print(i)
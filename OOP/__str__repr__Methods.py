# ()__str__()it is use to compute the "informal" string representation of an object.
# when we call print function this __str__() is automatically called. print(a.__str__())
# __repr__() is use rto compute the "official" string representation of an object.


print(str(1))
print(repr(1))
print(str("mehedi")) # it print just the content of the string
print(repr("mehedi")) # it is used for debugging

class cart:
    def __init__(self,item):
        self.item=item
    def __repr__(self):
        return ('Cart({})'.format(self.item))
    def __str__(self):
        return ('{}'.format(self.item))


obj=cart("mehedi")

print(repr(obj))
print(str(obj))

# they works by this way

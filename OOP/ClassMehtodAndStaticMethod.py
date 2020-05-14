#self is a instance variable
# we can not call instance method (method including self) with out creating the instance of this class
# if we want to update any class attribute(list,dict,tuple, variable) then no need to create instance of this class we can do it by class method @classmethod(decorator)
#class method contains cls parameter. it represent class itself, and it does not have any self parameter, as self is a instance variable
# we can directly call class method by class but we can not call instance method.

class Library:
    books=['a','b','c','d']
    def __init__(self,id,title):
        self.id=id
        self.title=title
    def requestbook(self):
        try:
            Library.books.remove(self.title)
            return 'Thank you.You can get the book '+self.title
        except:
            return self.title+" is not available now in library."

    @classmethod
    def updatebook(cls,lis):
        cls.books.extend(lis) #cls is Library
        print('updated library',cls.books)
    @staticmethod
    def Iamsatic(name): #it only deals with the parameter that we have passed.
        print("your name is ",name)
        #print('your id is',Library.books) # note it can not access any instance attribute. but it can access class attribute.

#Library.requestbook() we can not call instance method without creating the instance of class. it produce error.

st1=Library(8421,'v')
v=st1.requestbook() #Library.requestbook(st1)
print(v)

#now we want to update class attribute book. we can do it by the creating class method.

Library.updatebook(['m','n']) # process of calling class method.

#################static method##################
# a static method is a method that knows nothing about the class of instance it was called on.
# The parameter cls/self are not passed as implicit first arguments to the static method.

st1.Iamsatic("mehedi") # it deals with only mehedi


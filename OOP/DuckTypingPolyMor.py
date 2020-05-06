# If there is a bards which is walking like a duck which is quacking like a duck and which i swimming like a duck then that bird is a duck

# python support dynamic typing that means x=9 here x is integer. x= "m" here x is string

class PyCharm:
    def execute(self):
        print("Pycharm has:" )
        print("graph")
        print("debugging")


class MyEditor:
    def execute(self):
        print("My editor has:")
        print("convention check")
        print("spell check")

class Laptop:
    def code(self,ide):
        ide.execute()

lap=Laptop()
ide=PyCharm()

#pycharm and my editor both have execute function so if we want to my editor then if we change only ide=MyEditor() then we can easily access that. It is known as DuckTyping.


Laptop.code(lap,ide) # lap refers self that always refer instance an ide refer ide




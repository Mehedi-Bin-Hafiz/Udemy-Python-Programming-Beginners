print(dir())
# what is __name__
print(__name__) #__name__ assign the value __main__
# what is __main__ ans: main is a static point of execution.


from ModulesAndPackages.NotMain import runme
runme()

print("but current function __name__ ",__name__)



###
a=1
b=8

try:
    print(a/b)
except TypeError:
    print("please check the type of variable")
except ZeroDivisionError:
    print('divide by zero is impossible')
except:  # it is call generic except type.
    print("there is an error")
finally:
    print("I always execute even there is no error")


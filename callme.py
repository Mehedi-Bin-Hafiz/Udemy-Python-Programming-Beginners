




def ad(a,b):
    return a+b


if __name__=='__main__': # now after importing, other file not access next 2 line. because when it run itself then it retrun __main__ and when return main if condition is execute otherwise not
    print("Never call me without callme module. it is my own calculation")
    print(ad(12,13))
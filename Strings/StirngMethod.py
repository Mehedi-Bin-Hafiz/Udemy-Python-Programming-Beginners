# using object.method()

M="Mehedi Hasan"
print(M.upper())
print(M.lower())
print(M.capitalize()) #capitalize method convert first char to upper case others lowercase

# these method can not change original string for example
print(M)
# count method
print(M.count("e"))
# isupper islower method
print(M.isupper())
#replace method replace any one or more chars by another string but nor permanently
print(M.replace('i','y'))

# startswith() method can be use to check first char in a string
print(M.startswith('M'))
print(M.startswith('O'))
# to find the index of char we can use index() method
print(M.index('e')) # It always return first index

# VVI split Method split string and returns as a list
N= M.split()
print(N)
# for generating single cahr
p=list(M)
print(p)

#len() mehtod to find length of strings
print(len(M))

# String membership test
print("Me" in M)
print("Me" not in M)
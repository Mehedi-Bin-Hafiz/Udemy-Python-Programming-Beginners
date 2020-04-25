#String objects have a built-in operation using the % (modulo) operator which you can to format strings
#str.format() is a method
"""%s specify string %d specify integer number %f specify floating point number"""

print("my name is %s. I am %d years old. And I have %f taka." % ("mehedi",24,13.13)) # modulo operator is very important here

# String formatting using {}.format The main opportunity of using this is it maintain index number and we can moderate floating point number

print("my name is {}. I am {} years old. And I have {:.2f} taka.".format("mehedi",24,13.13))

print("my name is {0}. I am {2} years old. And I have {1:.2f} taka.".format("mehedi",24,13.13))


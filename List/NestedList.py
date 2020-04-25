# List inside list is called nested list
# nested list counted as one single element
ns=[1,2,3,[4,5,6,[7,'find me',9],7,8,9],4,5,6]
# if we want to find "find me " then we write code this way
print(ns[3][3][1])
#python file
# f=open("myimage.png",'rb')
# x=f.read()
# print(x)
f=open("text.txt",'w')
f.write("mehedi hasan  \n mahim hasan ")
f.close()
f=open("text.txt",'r')
# for i in f.read():
#     print(i)
#readlines returns list

x=f.readlines()
print(x)
f.close()
f=open("text.txt",'r')
y=f.read()
print(y)
#by seek method we can move cursor our defined index location
print(f.seek(3))
#by tell method we can see the current position of cursor
print(f.tell())

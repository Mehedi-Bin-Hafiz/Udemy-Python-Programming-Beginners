st="country"
m=st[:]
print(m) #print all the char
m=st[:3]  #[start index : end index : interval] by default start and interval is 0
print(m)
m=st[3:] #starting at 0 ending at the last of the len
print(m)
m=st[1:4:2]
print("st[1:4:2]",m,sep=" ")
m=st[-1] # represent last char
print(m)

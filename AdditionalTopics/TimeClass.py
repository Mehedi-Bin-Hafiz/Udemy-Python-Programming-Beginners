#Datetime.py
# class :
# Time , Date, Datetime, Timedelta

# What is timestamp?
# ans: Timestamp is a current time of an event that is recorded by a computer.

import datetime
T1 = datetime.time(12,30,20,100) #time(hour,min,sec,ms)

print(T1)
# if we can set new time we can do it by  creating new object of T1.
T2=T1.replace(11,23,49)
print(T2)

# print individually

print(T2.hour)


print(T1>T2)

print(T2.strftime('%H: %M: %S' ))

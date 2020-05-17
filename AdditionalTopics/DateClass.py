import datetime
d1=datetime.date(2019,7,21)
print(d1)
d2=d1.replace(2018,7,21)
print(d2)

print(datetime.date.today().strftime('%d %B %Y'))

print("sunday",datetime.date.today().weekday())

#########Struct_time object##########

print(datetime.date.today().timetuple())

print(datetime.date.fromtimestamp(0)) #timestamp is represented by second of unix time start from 1st january of 1970

print(datetime.date.fromtimestamp(904892345))



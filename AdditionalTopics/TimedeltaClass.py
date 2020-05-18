# A timedelta is a duration expressing the difference between two date/datetime object
# it is normally used to add or remove a certain duration of time from date/datetime objects.

# it has the following attributes: days, seconds, microseconds, milliseconds, minutes, hours, weeks.

from datetime import date, datetime, timedelta


# time delta always return days
delta=timedelta(weeks=1,days=1,minutes=20,hours=6,microseconds=1000)
print(delta)

print(delta.days)   ##note## weeks and days converted to days
print(delta.seconds)  ##minutes hours converted to seconds
print(delta.microseconds)  ## millisecond converted to microseconds

#add two datetime objects

dt1 = datetime(2019,7,1,12,23,46)
dt2 = datetime(2020,7,1,12,23,46)

dt3=dt1-dt2

print(dt2+dt3) ##VVI
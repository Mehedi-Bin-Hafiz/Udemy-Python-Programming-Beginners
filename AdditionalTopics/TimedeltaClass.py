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

